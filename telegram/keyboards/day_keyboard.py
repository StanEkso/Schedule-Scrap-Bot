from shared.types.callback import CallbackData
from shared.localization.service import localization
from telegram.keyboards.factory import KeyboardFactory

KEYBOARD_LOCALE = localization.getRawKeyboard()
# List of days for choosing
DAYS_CALLBACKS = ["day_mon", "day_tue",
                  "day_wed", "day_thu", "day_fri", "day_sat"]


KBOARD_BUTTONS_TEXTS = ["◀", KEYBOARD_LOCALE["ok"], "▶", KEYBOARD_LOCALE["monday"], KEYBOARD_LOCALE["tuesday"], KEYBOARD_LOCALE["wednesday"], KEYBOARD_LOCALE["thursday"], KEYBOARD_LOCALE["friday"], KEYBOARD_LOCALE["saturday"]
                        ]
KBOARD_BUTTONS_CALLBACKS = [CallbackData.PREV_DAY.value, CallbackData.HIDE_DETAILS.value, CallbackData.NEXT_DAY.value, CallbackData.DAY_PREFIX.value+"mon",
                            CallbackData.DAY_PREFIX.value+"tue", CallbackData.DAY_PREFIX.value+"wed", CallbackData.DAY_PREFIX.value+"thu", CallbackData.DAY_PREFIX.value+"fri", CallbackData.DAY_PREFIX.value+"sat"]

buttons = [KeyboardFactory.createInlineKeyboardButton(i[0], i[1]) for i in zip(
    KBOARD_BUTTONS_TEXTS, KBOARD_BUTTONS_CALLBACKS)]
DAY_CHOOSING_KEYBOARD = KeyboardFactory.createReplyMarkup(buttons, 3)
