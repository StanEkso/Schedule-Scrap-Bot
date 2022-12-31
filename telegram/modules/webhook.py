from aiogram.types import Message
from aiogram import Bot
from telegram.keyboards.show_keyboard import SHOW_SCHEDULE_KEYBOARD
from telegram.keyboards.day_keyboard import DAY_CHOOSING_KEYBOARD, DAYS_CALLBACKS
from telegram.keyboards.close_keyboard import CLOSE_SCHEDULE_KEYBOARD
from telegram.services.message import messageService
from telegram.services.schedule import scheduleService
from telegram.services.config import configService
from telegram.structures.hash import IntegerHash

from aiogram.dispatcher.webhook import SendMessage, DeleteMessage, EditMessageText


def messageToId(message: Message) -> str:
    return str(message.chat.id) + "_" + str(message.message_id)


hash = IntegerHash()


class ScheduleWebhookController:
    def __init__(self, ) -> None:
        pass

    async def showEnterMessage(self, message: Message):
        await message.answer(text=messageService.get("show"), reply_markup=SHOW_SCHEDULE_KEYBOARD)
        if (configService.get("DELETE_COMMANDS") == True):
            try:
                # await message.delete()
                return DeleteMessage(chat_id=message.chat.id, message_id=message.message_id)
            except:
                pass

    async def editSchedule(self, bot: Bot, message: Message, day: str):
        INDEX = DAYS_CALLBACKS.index(day)
        hash.set(key=messageToId(message), value=INDEX)
        await EditMessageText(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )

    async def showSchedule(self, message: Message):
        if (configService.get("UPDATE_ON_EVERY_SHOW") == True or hash.get(key=messageToId(message)) is None):
            scheduleService.update()
        hash.set(messageToId(message), 0)
        if (hash.get(key=messageToId(message)) is None):
            await SendMessage(chat_id=message.chat.id, text=scheduleService.atDay(0), reply_markup=DAY_CHOOSING_KEYBOARD)
        else:
            await EditMessageText(chat_id=message.chat.id, text=scheduleService.atDay(0), reply_markup=DAY_CHOOSING_KEYBOARD)

    async def sendNextDaySchedule(self, bot: Bot, message: Message):
        INDEX = hash.get(key=messageToId(message)) or 0
        if (INDEX > 4):
            INDEX = 0
        else:
            INDEX += 1

        await EditMessageText(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )
        hash.set(key=messageToId(message), value=INDEX)

    async def sendPrevDaySchedule(self, bot: Bot, message: Message):
        INDEX = hash.get(key=messageToId(message)) or 0
        if (INDEX < 1):
            INDEX = 5
        else:
            INDEX -= 1

        await EditMessageText(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=scheduleService.atDay(INDEX),
            reply_markup=DAY_CHOOSING_KEYBOARD
        )
        hash.set(key=messageToId(message), value=INDEX)

    async def hideSchedule(self, bot: Bot, message: Message):
        await EditMessageText(
            chat_id=message.chat.id,
            message_id=message.message_id,
            text=messageService.get("closed"),
            reply_markup=CLOSE_SCHEDULE_KEYBOARD
        )

    async def deleteScheduleMessage(self, bot: Bot, message: Message):
        await DeleteMessage(chat_id=message.chat.id,
                            message_id=message.message_id)


scheduleController = ScheduleWebhookController()
