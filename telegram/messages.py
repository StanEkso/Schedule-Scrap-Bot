from aiogram.types import Message, ContentType
from .decorators.logger import LogMessage
from shared.services.config import configService
from .modules.schedule.controller import scheduleController
from .__init__ import dp


def init():
    @dp.message_handler(commands=configService.get("SCHEDULE_COMMANDS") or ["schedule"])
    @LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
    async def handleSchedule(message: Message, *args, **kwargs):
        return await scheduleController.showEnterMessage(message)

    @dp.message_handler(content_types=ContentType.TEXT)
    @LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
    async def handleText(message: Message, *args, **kwargs):
        pass

    pass
