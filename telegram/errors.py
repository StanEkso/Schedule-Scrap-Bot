from .__init__ import dp
from aiogram.types import Update


def init():

    @dp.errors_handler()
    async def message_not_modified_handler(update: Update, error):
        print("[ERROR] " + str(error))
        return error
