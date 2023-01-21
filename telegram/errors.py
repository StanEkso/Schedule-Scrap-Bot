from .__init__ import dp
from aiogram.types import Update
from shared.logger.logger import logger


async def unhandledErrorHandler(update: Update, error):
    logger.error(str(error))
    return error


def init():
    dp.register_errors_handler(unhandledErrorHandler)
