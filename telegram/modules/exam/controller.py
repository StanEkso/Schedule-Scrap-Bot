from aiogram.types import Message
from .service import examsService
class ExamController:
    async def handleExamMessage(self, message: Message):
        return await message.answer(text=examsService.get()) 
