from aiogram.types import Message
from .service import examsService
from ..keyboard.close_exam_keyboard import CLOSE_EXAM_SCHEDULE
from ..message.controller import messageController


class ExamController:
    async def handleExamMessage(self, message: Message):
        await message.answer(text=examsService.get(), reply_markup=CLOSE_EXAM_SCHEDULE)
        await messageController.deleteMessageIfRequired(message)


examController = ExamController()
