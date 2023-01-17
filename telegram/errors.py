from .__init__ import dp
from aiogram.types import Update


async def unhandledErrorHandler(update: Update, error):
    print("[ERROR] " + str(error))
    return error


def init():
    dp.register_errors_handler(unhandledErrorHandler)
