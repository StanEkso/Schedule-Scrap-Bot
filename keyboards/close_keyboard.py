from aiogram import types
from customtypes.callback import CallbackData

CLOSE_SCHEDULE_KEYBOARD = types.InlineKeyboardMarkup()
show = types.InlineKeyboardButton(
    text="Просмотреть", callback_data=CallbackData.SHOW_SCHEDULE.value)
close = types.InlineKeyboardButton(
    text="Убрать сообщение", callback_data=CallbackData.CLOSE_SCHEDULE.value)
CLOSE_SCHEDULE_KEYBOARD.add(show)
CLOSE_SCHEDULE_KEYBOARD.row()
CLOSE_SCHEDULE_KEYBOARD.add(close)
