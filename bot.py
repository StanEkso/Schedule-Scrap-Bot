import os
from aiogram import executor
from telegram.main import dp, WEBAPP_HOST, on_startup, on_shutdown, WEBHOOK_PATH, WEBAPP_PORT
if __name__ == '__main__':
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
