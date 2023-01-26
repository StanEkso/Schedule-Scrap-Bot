import asyncio
from .callback_queries import init as callbackQueriesInit
from .messages import init as messagesInit
from .errors import init as errorsInit
from aiogram import Dispatcher
from aiogram.utils.executor import set_webhook
from aiohttp.web import Application
from shared.logger.logger import logger


from .__init__ import bot, dp
from .__run__ import WEBHOOK_URL


def bootstrap():
    messagesInit()
    callbackQueriesInit()
    errorsInit()
    logger.init("Telegram bot is initialized")

    def initWebhook(WEBHOOK_PATH: str, app: Application):
        logger.init("Webhook is initialized")
        set_webhook(dispatcher=dp,
                    webhook_path=WEBHOOK_PATH,
                    web_app=app,
                    skip_updates=True,
                    on_startup=on_startup,
                    on_shutdown=on_shutdown,
                    )

    return bot, dp, initWebhook


async def on_startup(dispatcher: Dispatcher):
    await dispatcher.bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    # await dispatcher.bot.delete_webhook(drop_pending_updates=True)
    pass


def bootstrap_bot():
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(log_bot_info())


async def log_bot_info():
    me = await bot.get_me()
    FIRST_NAME = me.first_name or ''
    LAST_NAME = me.last_name or ''
    USERNAME = me.username or ''

    logger.init(f"Bot: {FIRST_NAME} {LAST_NAME} (@{USERNAME})")
