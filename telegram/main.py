import asyncio
from .callback_queries import init as callbackQueriesInit
from .messages import init as messagesInit
from .errors import init as errorsInit
from aiogram import executor, Dispatcher


from .__init__ import bot, dp
from .__run__ import WEBHOOK_URL


messagesInit()
callbackQueriesInit()
errorsInit()


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

    print(f"[INIT] Current session: {FIRST_NAME} {LAST_NAME} (@{USERNAME})")
