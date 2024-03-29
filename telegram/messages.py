from aiogram.types import Message, ContentType

from .modules.exam.controller import exam_controller
from .decorators.logger import LogMessage
from shared.services.config import config_service
from .modules.schedule.controller import scheduleController
from .__init__ import dp


@LogMessage(show_time=True, show_chat_type=True)
async def handleSchedule(message: Message, *args, **kwargs):
    return await scheduleController.showEnterMessage(message)


@LogMessage(show_time=True, show_chat_type=True)
async def handleText(message: Message, *args, **kwargs):
    pass


@LogMessage(show_time=True, show_chat_type=True)
async def handleExam(message: Message, *args, **kwargs):
    return await exam_controller.handle_exam_message(message)


def init():
    SCHEDULE_COMMANDS = config_service.get("SCHEDULE_COMMANDS") or ["schedule"]
    dp.register_message_handler(handleSchedule, commands=SCHEDULE_COMMANDS)

    EXAMS_COMMANDS = config_service.get("EXAMS_COMMANDS") or ["exams"]
    dp.register_message_handler(handleExam, commands=EXAMS_COMMANDS)
    dp.register_message_handler(handleText, content_types=ContentType.TEXT)
