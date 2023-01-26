from telegram.__run__ import WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, USE_MODE
from web.api import bootstrap as apiBootstrap
from aiogram import executor
from aiohttp import web
from telegram.main import bootstrap as tgBootstrap
from shared.logger.logger import logger


def bootstrap():
    if (USE_MODE == 'WEBHOOK'):
        logger.init("Webhook mode is enabled")
        bot, dp, initWebhook = tgBootstrap()
        app = apiBootstrap()
        app["bot"] = bot
        initWebhook(WEBHOOK_PATH, app)

        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    elif (USE_MODE == 'API'):
        logger.init("API mode is enabled")
        app = apiBootstrap()
        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
    else:
        logger.init("Long polling mode is enabled")
        bot, dp, initWebhook = tgBootstrap()
        executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    bootstrap()
