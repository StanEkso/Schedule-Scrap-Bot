from aiogram import types

from customtypes.callback import CallbackData

SHOW_SCHEDULE_KEYBOARD = types.InlineKeyboardMarkup()
show = types.InlineKeyboardButton(
    text="Просмотреть", callback_data=CallbackData.SHOW_SCHEDULE.value)
SHOW_SCHEDULE_KEYBOARD.add(show)
