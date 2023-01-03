from aiogram.types import Message
from aiogram import Bot
from telegram.keyboards.show_keyboard import SHOW_SCHEDULE_KEYBOARD
from telegram.keyboards.day_keyboard import DAY_CHOOSING_KEYBOARD, DAYS_CALLBACKS
from telegram.keyboards.close_keyboard import CLOSE_SCHEDULE_KEYBOARD
from telegram.services.message import messageService
from telegram.services.schedule import scheduleService
from shared.services.config import configService
from telegram.structures.hash import IntegerHash


def messageToId(message: Message) -> str:
    return str(message.chat.id) + "_" + str(message.message_id)


hash = IntegerHash()


class ScheduleController:
    # Method to show enter message
    async def showEnterMessage(self, message: Message):
        await message.answer(text=messageService.get("show"), reply_markup=SHOW_SCHEDULE_KEYBOARD)
        if (configService.get("DELETE_COMMANDS") == True):
            try:
                await message.delete()
            except:
                pass

    # Method to edit existing schedule with new day
    async def editSchedule(self, bot: Bot, message: Message, day: str):
        # Get index of day using callback data
        INDEX = DAYS_CALLBACKS.index(day)

        # Set index to hash
        hash.set(key=messageToId(message), value=INDEX)
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )

    async def showSchedule(self, message: Message):
        # Check if schedule should be updated on every show
        if (configService.get("UPDATE_ON_EVERY_SHOW") == True or hash.get(key=messageToId(message)) is None):
            scheduleService.update()

        # Set default index to hash
        hash.set(messageToId(message), 0)
        if (hash.get(key=messageToId(message)) is None):
            # If message isn't exist, send new message
            await message.answer(text=scheduleService.atDay(0), reply_markup=DAY_CHOOSING_KEYBOARD)
        else:
            # If message is exist, edit it
            await message.edit_text(text=scheduleService.atDay(0), reply_markup=DAY_CHOOSING_KEYBOARD)

    async def sendNextDaySchedule(self, bot: Bot, message: Message):
        # Get index of day using hash
        INDEX = hash.get(key=messageToId(message)) or 0
        # Get new index by direction
        NEW_INDEX = self.getNewIndex(INDEX, 1)

        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(NEW_INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )
        hash.set(key=messageToId(message), value=NEW_INDEX)

    async def sendPrevDaySchedule(self, bot: Bot, message: Message):
        # Get index of day using hash
        INDEX = hash.get(key=messageToId(message)) or 0
        # Get new index by direction
        NEW_INDEX = self.getNewIndex(INDEX, -1)

        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(NEW_INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )
        hash.set(key=messageToId(message), value=NEW_INDEX)

    async def hideSchedule(self, bot: Bot, message: Message):
        # Hide schedule message
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=messageService.get("closed"),
            reply_markup=CLOSE_SCHEDULE_KEYBOARD
        )

    async def deleteScheduleMessage(self, bot: Bot, message: Message):
        # Delete message from chat
        await bot.delete_message(chat_id=message.chat.id,
                                 message_id=message.message_id)

    def getNewIndex(self, index: int, direction: int = 1) -> int:
        # Get new index by direction
        # Index + direction can't be less than 0 or more than 5
        if (index + direction > 5):
            # If index + direction is more than 5, return 0, cause 5 is saturday
            return 0
        elif (index + direction < 0):
            # If index + direction is less than 0, return 5, cause 0 is monday
            return 5
        # Return index + direction in other cases
        return index + direction


scheduleController = ScheduleController()
