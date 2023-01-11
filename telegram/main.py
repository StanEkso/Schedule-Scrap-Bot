import asyncio
from .callback_queries import init as callbackQueriesInit
from .messages import init as messagesInit
from .errors import init as errorsInit
from aiogram import executor, Dispatcher

from aiogram.utils.executor import set_webhook
from aiohttp import web

from .__init__ import bot, dp
from .__run__ import WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_HOST, WEBAPP_PORT, USE_MODE

from .web_app import routes as webRoutes

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

    if (USE_MODE == 'WEBHOOK'):
        print("[INIT] Webhook mode is enabled.")
        app = web.Application()
        app["bot"] = bot
        app.add_routes(webRoutes)
        set_webhook(dispatcher=dp,
                    webhook_path=WEBHOOK_PATH,
                    web_app=app,
                    skip_updates=True,
                    on_startup=on_startup,
                    on_shutdown=on_shutdown,

                    )

        web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)            
        # executor.start_webhook(
        #     dispatcher=dp,
        #     webhook_path=WEBHOOK_PATH,
        #     skip_updates=True,
        #     on_startup=on_startup,
        #     on_shutdown=on_shutdown,
        #     host=WEBAPP_HOST,
        #     port=WEBAPP_PORT
        # )
    else:
        print("[INIT] Long polling mode is enabled.")
        executor.start_polling(dp, skip_updates=True)


async def log_bot_info():
    me = await bot.get_me()
    FIRST_NAME = me.first_name or ''
    LAST_NAME = me.last_name or ''
    USERNAME = me.username or ''

    print(f"[INIT] Current session: {FIRST_NAME} {LAST_NAME} (@{USERNAME})")
