from aiogram.types import Message
from .service import examsService
from shared.services.config import configService
from ..keyboard.close_exam_keyboard import CLOSE_EXAM_SCHEDULE

class ExamController:
    async def handleExamMessage(self, message: Message):
        await message.answer(text=examsService.get(), reply_markup=CLOSE_EXAM_SCHEDULE)
        if (configService.get("DELETE_COMMANDS") == True):
            try:
                await message.delete()
            except:
                pass

    async def closeExamMessage(self, message: Message):
        try:
            await message.delete()
        except:
            pass


examController = ExamController()
