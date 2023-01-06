from .callback_queries import init as callbackQueriesInit
from .messages import init as messagesInit
from aiogram import executor

from .__init__ import bot, dp
from .__run__ import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT, MODE


# Bot handling messages
messagesInit()
callbackQueriesInit()


@dp.errors_handler()
async def message_not_modified_handler(update, error):
    print(error)
    return error


async def on_startup(dispatcher):
    BOT_INFO = await bot.get_me()
    print("[INFO] Starting bot: ", BOT_INFO)
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    pass


def bootstrap_bot():
    print("Starting bot...")
    if (MODE == 'WEBHOOK'):
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
