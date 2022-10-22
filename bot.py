from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from services.config import configService as configService
from controllers.schedule import scheduleController
bot = Bot(token=configService.get("token"), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['расписание', 'schedule'])
async def handleSchedule(message: types.Message):
    return await scheduleController.showEnterMessage(message)


@dp.callback_query_handler(lambda call: call.data == "show")
async def handleShowSchedule(call: types.CallbackQuery):
    return await scheduleController.showSchedule(call.message)


@dp.callback_query_handler(lambda call: call.data.find("day_") != -1)
async def handleShowSchedule(call: types.CallbackQuery):
    return await scheduleController.editSchedule(bot, call.message, call.data)


@dp.callback_query_handler(lambda call: call.data == "next")
async def handleNextDaySchedule(call: types.CallbackQuery):
    return await scheduleController.sendNextDaySchedule(bot, call.message)


@dp.callback_query_handler(lambda call: call.data == "next")
async def handlePrevDaySchedule(call: types.CallbackQuery):
    return await scheduleController.sendPrevDaySchedule(bot, call.message)


@dp.callback_query_handler(lambda call: call.data == "ok")
async def handlePrevDaySchedule(call: types.CallbackQuery):
    return await scheduleController.hideSchedule(bot, call.message)


@dp.callback_query_handler(lambda call: call.data == "close")
async def handlePrevDaySchedule(call: types.CallbackQuery):
    return await scheduleController.deleteScheduleMessage(bot, call.message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
