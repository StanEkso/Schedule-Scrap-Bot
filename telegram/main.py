import asyncio
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from telegram.services.config import configService
from telegram.controllers.schedule import scheduleController as pollingController
from telegram.modules.webhook import scheduleController as webhookController
from telegram.customtypes.callback import CallbackData

bot = Bot(token=configService.get("token"), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

scheduleController = pollingController


async def bootstrapBot():
    print(await bot.get_me())


@dp.message_handler(commands=configService.get("SCHEDULE_COMMANDS") or ["schedule"])
async def handleSchedule(message: types.Message):
    return await scheduleController.showEnterMessage(message)


@dp.callback_query_handler(lambda call: call.data == CallbackData.SHOW_SCHEDULE.value)
async def handleShowSchedule(call: types.CallbackQuery):
    return await scheduleController.showSchedule(call.message)


@dp.callback_query_handler(lambda call: call.data.find(CallbackData.DAY_PREFIX.value) != -1)
async def handleShowSchedule(call: types.CallbackQuery):
    return await scheduleController.editSchedule(bot, call.message, call.data)


@dp.callback_query_handler(lambda call: call.data == CallbackData.NEXT_DAY.value)
async def handleNextDaySchedule(call: types.CallbackQuery):
    return await scheduleController.sendNextDaySchedule(bot, call.message)


@dp.callback_query_handler(lambda call: call.data == CallbackData.PREV_DAY.value)
async def handlePrevDaySchedule(call: types.CallbackQuery):
    return await scheduleController.sendPrevDaySchedule(bot, call.message)


@dp.callback_query_handler(lambda call: call.data == CallbackData.HIDE_DETAILS.value)
async def handlePrevDaySchedule(call: types.CallbackQuery):
    return await scheduleController.hideSchedule(bot, call.message)


@dp.callback_query_handler(lambda call: call.data == CallbackData.CLOSE_SCHEDULE.value)
async def handlePrevDaySchedule(call: types.CallbackQuery):
    return await scheduleController.deleteScheduleMessage(bot, call.message)


@dp.errors_handler()
async def message_not_modified_handler(update, error):
    print(error)
    return error

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
WEBHOOK_ENDPOINT = os.getenv("WEBHOOK_ENDPOINT", "")

WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{WEBHOOK_ENDPOINT}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv("PORT", 8000)
print(WEBAPP_PORT)


async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    # await bot.delete_webhook()
    pass


def bootstrap_bot():
    print("Starting bot...")
    if (os.getenv("USE", 'POLLING') == 'WEBHOOK'):
        executor.start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            skip_updates=True,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT
        )
    else:
        executor.start_polling(dp, skip_updates=True)