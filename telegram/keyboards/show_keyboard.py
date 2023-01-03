from aiogram import types
from telegram.customtypes.callback import CallbackData

# Keyboard showed when command /schedule is called
SHOW_SCHEDULE_KEYBOARD = types.InlineKeyboardMarkup()
show = types.InlineKeyboardButton(
    text="Просмотреть", callback_data=CallbackData.SHOW_SCHEDULE.value)
SHOW_SCHEDULE_KEYBOARD.add(show)
