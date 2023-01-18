from aiogram.types import Message
from .service import examsService
from shared.services.config import configService

class ExamController:
    async def handleExamMessage(self, message: Message):
        await message.answer(text=examsService.get())
        if (configService.get("DELETE_COMMANDS") == True):
            try:
                await message.delete()
            except:
                pass


examController = ExamController()
