from aiogram import types
from telegram.customtypes.callback import CallbackData
from shared.localization.service import localization

KEYBOARD_LOCALE = localization.getRawKeyboard()
# List of days for choosing
DAYS_CALLBACKS = ["day_mon", "day_tue",
                  "day_wed", "day_thu", "day_fri", "day_sat"]
DAY_CHOOSING_KEYBOARD = types.InlineKeyboardMarkup()

# Buttons for choosing day, with callback data for each day "day_{day}"
buttonPrev = types.InlineKeyboardButton(
    text="◀", callback_data=CallbackData.PREV_DAY.value)
buttonOK = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["ok"], callback_data=CallbackData.HIDE_DETAILS.value)
buttonNext = types.InlineKeyboardButton(
    text="▶", callback_data=CallbackData.NEXT_DAY.value)
buttonMon = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["monday"], callback_data=CallbackData.DAY_PREFIX.value+"mon")
buttonTue = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["tuesday"], callback_data=CallbackData.DAY_PREFIX.value+"tue")
buttonWed = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["wednesday"], callback_data=CallbackData.DAY_PREFIX.value+"wed")
buttonThu = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["thursday"], callback_data=CallbackData.DAY_PREFIX.value+"thu")
buttonFri = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["friday"], callback_data=CallbackData.DAY_PREFIX.value+"fri")
buttonSat = types.InlineKeyboardButton(
    text=KEYBOARD_LOCALE["saturday"], callback_data=CallbackData.DAY_PREFIX.value+"sat")

# Constructing keyboard
DAY_CHOOSING_KEYBOARD.add(buttonPrev, buttonOK, buttonNext)
DAY_CHOOSING_KEYBOARD.row()
DAY_CHOOSING_KEYBOARD.add(buttonMon, buttonTue, buttonWed)
DAY_CHOOSING_KEYBOARD.row()
DAY_CHOOSING_KEYBOARD.add(buttonThu, buttonFri, buttonSat)
