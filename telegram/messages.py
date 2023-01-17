from aiogram.types import Message, ContentType
from .decorators.logger import LogMessage
from shared.services.config import configService
from .modules.schedule.controller import scheduleController
from .__init__ import dp


@LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
async def handleSchedule(message: Message, *args, **kwargs):
    return await scheduleController.showEnterMessage(message)


@LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
async def handleText(message: Message, *args, **kwargs):
    pass


def init():
    dp.register_message_handler(handleSchedule, commands=configService.get(
        "SCHEDULE_COMMANDS") or ["schedule"])

    dp.register_message_handler(handleText, content_types=ContentType.TEXT)

