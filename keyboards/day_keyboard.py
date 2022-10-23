from aiogram import types

from customtypes.callback import CallbackData
DAYS_CALLBACKS = ["day_mon", "day_tue",
                  "day_wed", "day_thu", "day_fri", "day_sat"]
DAY_CHOOSING_KEYBOARD = types.InlineKeyboardMarkup()
buttonPrev = types.InlineKeyboardButton(
    text="◀", callback_data=CallbackData.PREV_DAY.value)
buttonOK = types.InlineKeyboardButton(text="OK", callback_data="ok")
buttonNext = types.InlineKeyboardButton(text="▶", callback_data='next')
buttonMon = types.InlineKeyboardButton(text="ПН", callback_data="day_mon")
buttonTue = types.InlineKeyboardButton(text="ВТ", callback_data="day_tue")
buttonWed = types.InlineKeyboardButton(text="СР", callback_data="day_wed")
buttonThu = types.InlineKeyboardButton(text="ЧТ", callback_data="day_thu")
buttonFri = types.InlineKeyboardButton(text="ПТ", callback_data="day_fri")
buttonSat = types.InlineKeyboardButton(text="СБ", callback_data="day_sat")
DAY_CHOOSING_KEYBOARD.add(buttonPrev, buttonOK, buttonNext)
DAY_CHOOSING_KEYBOARD.row().add(buttonMon, buttonTue, buttonWed) \
    .row().add(buttonThu, buttonFri, buttonSat)
