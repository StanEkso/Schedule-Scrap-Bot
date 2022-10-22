from aiogram import types

SHOW_SCHEDULE_KEYBOARD = types.InlineKeyboardMarkup()
show = types.InlineKeyboardButton(text="Просмотреть", callback_data='show')
SHOW_SCHEDULE_KEYBOARD.add(show)
