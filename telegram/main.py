import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from shared.services.config import configService
from telegram.controllers.schedule import scheduleController
from telegram.decorators.failquery import OnQueryFail
from shared.localization.service import localization
from telegram.filters.callback import isCloseCallback, isDayCallback, isHideCallback, isNextDayCallback, isPrevDayCallback, isShowScheduleCallback
from telegram.decorators.logger import LogMessage, LogCall

bot = Bot(token=configService.get("token"), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Get bot info


async def bootstrapBot():
    print(await bot.get_me())


# Bot handle commands "/schedule"


@dp.message_handler(commands=configService.get("SCHEDULE_COMMANDS") or ["schedule"])
@LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
async def handleSchedule(message: types.Message, *args, **kwargs):
    return await scheduleController.showEnterMessage(message)


@dp.message_handler(content_types=types.ContentType.TEXT)
@LogMessage(SHOW_TIME=True, SHOW_CHAT_TYPE=True)
async def handleText(message: types.Message, *args, **kwargs):
    return await message.answer(message.text)

# Bot handle callback query "show_schedule"


@dp.callback_query_handler(isShowScheduleCallback)
@LogCall(SHOW_CHAT_TYPE=True)
async def handleShowSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.showSchedule(call.message)

# Bot handle callback query "day_{wd}"


@dp.callback_query_handler(isDayCallback)
@OnQueryFail(localization.getMessage("day_is_chosen"))
@LogCall(SHOW_CHAT_TYPE=True)
async def handleShowSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.editSchedule(call.message, call.data)

# Bot handle callback query "next_day"


@dp.callback_query_handler(isNextDayCallback)
@LogCall(SHOW_CHAT_TYPE=True)
async def handleNextDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.sendNextDaySchedule(call.message)

# Bot handle callback query "prev_day"


@dp.callback_query_handler(isPrevDayCallback)
@LogCall(SHOW_CHAT_TYPE=True)
async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.sendPrevDaySchedule(call.message)

# Bot handle callback query "hide_details"


@dp.callback_query_handler(isHideCallback)
@LogCall(SHOW_CHAT_TYPE=True)
async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.hideSchedule(call.message)

# Bot handle callback query "close_schedule"


@dp.callback_query_handler(isCloseCallback)
@LogCall(SHOW_CHAT_TYPE=True)
async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.deleteScheduleMessage(call.message)

# Bot handle errors


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

# Start webhook with aiohttp server


async def on_startup(dispatcher):
    BOT_INFO = await bot.get_me()
    print(f"Starting bot {BOT_INFO.username}...")
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)

# Shutdown webhook on shutdown (delete webhook), but don't await this task


async def on_shutdown(dispatcher):
    # await bot.delete_webhook()
    pass

# Function to start bot with webhook or polling


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
