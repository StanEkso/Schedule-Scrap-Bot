from aiogram import types
from telegram.customtypes.callback import CallbackData
from shared.localization.service import localization

KEYBOARD_LOCALE = localization.getRawKeyboard()
# Keyboard for closing schedule message
CLOSE_SCHEDULE_KEYBOARD = types.InlineKeyboardMarkup()
show = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["show"], callback_data=CallbackData.SHOW_SCHEDULE.value)
close = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["close"], callback_data=CallbackData.CLOSE_SCHEDULE.value)
CLOSE_SCHEDULE_KEYBOARD.add(show)
CLOSE_SCHEDULE_KEYBOARD.row()
CLOSE_SCHEDULE_KEYBOARD.add(close)
