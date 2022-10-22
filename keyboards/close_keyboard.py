from aiogram import types

CLOSE_SCHEDULE_KEYBOARD = types.InlineKeyboardMarkup()
show = types.InlineKeyboardButton(text="Просмотреть", callback_data='show')
close = types.InlineKeyboardButton(
    text="Убрать сообщение", callback_data='close')
CLOSE_SCHEDULE_KEYBOARD.add(show)
CLOSE_SCHEDULE_KEYBOARD.row()
CLOSE_SCHEDULE_KEYBOARD.add(close)
