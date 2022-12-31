from aiogram import types

from telegram.customtypes.callback import CallbackData
DAYS_CALLBACKS = ["day_mon", "day_tue",
                  "day_wed", "day_thu", "day_fri", "day_sat"]
DAY_CHOOSING_KEYBOARD = types.InlineKeyboardMarkup()
buttonPrev = types.InlineKeyboardButton(
    text="◀", callback_data=CallbackData.PREV_DAY.value)
buttonOK = types.InlineKeyboardButton(
    text="OK", callback_data=CallbackData.HIDE_DETAILS.value)
buttonNext = types.InlineKeyboardButton(
    text="▶", callback_data=CallbackData.NEXT_DAY.value)
buttonMon = types.InlineKeyboardButton(
    text="ПН", callback_data=CallbackData.DAY_PREFIX.value+"mon")
buttonTue = types.InlineKeyboardButton(
    text="ВТ", callback_data=CallbackData.DAY_PREFIX.value+"tue")
buttonWed = types.InlineKeyboardButton(
    text="СР", callback_data=CallbackData.DAY_PREFIX.value+"wed")
buttonThu = types.InlineKeyboardButton(
    text="ЧТ", callback_data=CallbackData.DAY_PREFIX.value+"thu")
buttonFri = types.InlineKeyboardButton(
    text="ПТ", callback_data=CallbackData.DAY_PREFIX.value+"fri")
buttonSat = types.InlineKeyboardButton(
    text="СБ", callback_data=CallbackData.DAY_PREFIX.value+"sat")
DAY_CHOOSING_KEYBOARD.add(buttonPrev, buttonOK, buttonNext)
DAY_CHOOSING_KEYBOARD.row().add(buttonMon, buttonTue, buttonWed) \
    .row().add(buttonThu, buttonFri, buttonSat)
