from telegram.__run__ import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, USE_MODE
from web.api import bootstrap as apiBootstrap
from aiogram.utils.executor import set_webhook
from aiogram import executor
from aiohttp import web
from telegram.main import on_shutdown, on_startup, bootstrap as tgBootstrap


# Start the bot

def bootstrap():
    if (USE_MODE == 'WEBHOOK'):
        print("[INIT] Webhook mode is enabled.")
        bot, dp = tgBootstrap()
        app = apiBootstrap()
        app["bot"] = bot
        set_webhook(dispatcher=dp,
                    webhook_path=WEBHOOK_PATH,
                    web_app=app,
                    skip_updates=True,
                    on_startup=on_startup,
                    on_shutdown=on_shutdown,
                    )

        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    elif (USE_MODE == 'API'):
        print("[INIT] API mode is enabled.")
        app = apiBootstrap()
        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    else:
        print("[INIT] Long polling mode is enabled.")
        bot, dp = tgBootstrap()
        executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    bootstrap()
