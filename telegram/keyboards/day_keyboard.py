from aiogram import types

from telegram.customtypes.callback import CallbackData
from shared.localization.service import localization
# List of days for choosing
DAYS_CALLBACKS = ["day_mon", "day_tue",
                  "day_wed", "day_thu", "day_fri", "day_sat"]
DAY_CHOOSING_KEYBOARD = types.InlineKeyboardMarkup()

# Buttons for choosing day, with callback data for each day "day_{day}"
buttonPrev = types.InlineKeyboardButton(
    text="◀", callback_data=CallbackData.PREV_DAY.value)
buttonOK = types.InlineKeyboardButton(
    text=localization.getKeyboard("ok"), callback_data=CallbackData.HIDE_DETAILS.value)
buttonNext = types.InlineKeyboardButton(
    text="▶", callback_data=CallbackData.NEXT_DAY.value)
buttonMon = types.InlineKeyboardButton(
    text=localization.getKeyboard("monday"), callback_data=CallbackData.DAY_PREFIX.value+"mon")
buttonTue = types.InlineKeyboardButton(
    text=localization.getKeyboard("tuesday"), callback_data=CallbackData.DAY_PREFIX.value+"tue")
buttonWed = types.InlineKeyboardButton(
    text=localization.getKeyboard("wednesday"), callback_data=CallbackData.DAY_PREFIX.value+"wed")
buttonThu = types.InlineKeyboardButton(
    text=localization.getKeyboard("thursday"), callback_data=CallbackData.DAY_PREFIX.value+"thu")
buttonFri = types.InlineKeyboardButton(
    text=localization.getKeyboard("friday"), callback_data=CallbackData.DAY_PREFIX.value+"fri")
buttonSat = types.InlineKeyboardButton(
    text=localization.getKeyboard("saturday"), callback_data=CallbackData.DAY_PREFIX.value+"sat")

# Constructing keyboard
DAY_CHOOSING_KEYBOARD.add(buttonPrev, buttonOK, buttonNext)
DAY_CHOOSING_KEYBOARD.row()
DAY_CHOOSING_KEYBOARD.add(buttonMon, buttonTue, buttonWed)
DAY_CHOOSING_KEYBOARD.row()
DAY_CHOOSING_KEYBOARD.add(buttonThu, buttonFri, buttonSat)
