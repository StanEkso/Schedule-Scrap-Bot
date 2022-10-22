from aiogram.types import Message
from aiogram import Bot
from keyboards.show_keyboard import SHOW_SCHEDULE_KEYBOARD
from keyboards.day_keyboard import DAY_CHOOSING_KEYBOARD, DAYS_CALLBACKS
from keyboards.close_keyboard import CLOSE_SCHEDULE_KEYBOARD
from services.message import messageService
from services.schedule import scheduleService
from structures.hash import Hash, IntegerHash


def messageToId(message: Message) -> str:
    return str(message.chat.id) + "_" + str(message.message_id)


hash = IntegerHash()


class ScheduleController:

    async def showEnterMessage(self, message: Message):
        await message.answer(text=messageService.get("show"), reply_markup=SHOW_SCHEDULE_KEYBOARD)

    async def editSchedule(self, bot: Bot, message: Message, day: str):
        INDEX = DAYS_CALLBACKS.index(day)
        print(INDEX)
        hash.set(key=messageToId(message), value=INDEX)
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )

    async def showSchedule(self, message: Message):
        scheduleService.update()
        hash.set(messageToId(message), 0)
        await message.answer(text=scheduleService.atDay(0), reply_markup=DAY_CHOOSING_KEYBOARD)

    async def sendNextDaySchedule(self, bot: Bot, message: Message):
        INDEX = hash.get(key=messageToId(message))
        if (INDEX > 4):
            INDEX = 0
        else:
            INDEX += 1

        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )
        hash.set(key=messageToId(message), value=INDEX)

    async def sendPrevDaySchedule(self, bot: Bot, message: Message):
        INDEX = hash.get(key=messageToId(message))
        if (INDEX < 1):
            INDEX = 5
        else:
            INDEX -= 1

        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )
        hash.set(key=messageToId(message), value=INDEX)

    async def hideSchedule(self, bot: Bot, message: Message):
        await bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=messageService.get("closed"),
            reply_markup=CLOSE_SCHEDULE_KEYBOARD
        )

    async def deleteScheduleMessage(self, bot: Bot, message: Message):
        await bot.delete_message(chat_id=message.chat.id,
                                 message_id=message.message_id)


scheduleController = ScheduleController()
