from aiogram import types
from telegram.customtypes.callback import CallbackData
from shared.localization.service import localization
KEYBOARD_LOCALE = localization.getRawKeyboard()
# Keyboard showed when command /schedule is called
SHOW_SCHEDULE_KEYBOARD = types.InlineKeyboardMarkup()
show = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE['show'], callback_data=CallbackData.SHOW_SCHEDULE.value)
SHOW_SCHEDULE_KEYBOARD.add(show)
