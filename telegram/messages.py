from aiogram.types import Message, ContentType

from .modules.exam.controller import examController
from .decorators.logger import LogMessage
from shared.services.config import config_service
from .modules.schedule.controller import scheduleController
from .__init__ import dp

from shared.services.parsing import parser_service
from shared.types.lesson import lessonToString
import json


@LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
async def handleSchedule(message: Message, *args, **kwargs):
    return await scheduleController.showEnterMessage(message)


@LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
async def handleText(message: Message, *args, **kwargs):
    pass


@LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
async def handleExam(message: Message, *args, **kwargs):
    return await examController.handleExamMessage(message)


def init():
    SCHEDULE_COMMANDS = config_service.get("SCHEDULE_COMMANDS") or ["schedule"]
    dp.register_message_handler(handleSchedule, commands=SCHEDULE_COMMANDS)

    EXAMS_COMMANDS = config_service.get("EXAMS_COMMANDS") or ["exams"]
    dp.register_message_handler(handleExam, commands=EXAMS_COMMANDS)
    dp.register_message_handler(handleText, content_types=ContentType.TEXT)
