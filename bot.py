import os
from aiogram import executor
from telegram.main import dp, WEBAPP_HOST, on_startup, on_shutdown, WEBHOOK_PATH, WEBAPP_PORT, bootstrap_bot
from api.main import app, bootstrap_api
from shared.services.parsing import parser


import asyncio
import threading

if __name__ == '__main__':
    apiThread = threading.Thread(target=bootstrap_api)
    apiThread.start()
    bootstrap_bot()
