from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from services.config import config as configService
bot = Bot(token=configService.get("token"), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['расписание', 'schedule'])
async def handleSchedule(message: types.Message):
    return await message.answer(123)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
