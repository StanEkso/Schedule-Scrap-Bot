from aiogram.types import Message
from .service import exams_service
from ..keyboard.close_exam_keyboard import CLOSE_EXAM_SCHEDULE
from ..message.controller import messageController


class ExamController:
    async def handle_exam_message(self, message: Message):
        await message.answer(text=exams_service.get(), reply_markup=CLOSE_EXAM_SCHEDULE)
        await messageController.delete_message_if_required(message)

    async def close_exam_message(self, message: Message):
        await message.delete()


exam_controller = ExamController()
