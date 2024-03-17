from shared.types.callback import CallbackData
from shared.localization.service import localization_service
from .factory import KeyboardFactory

KEYBOARD_LOCALE = localization_service.get_keyboard_dict()
# List of days for choosing
DAYS_CALLBACKS = ["day_mon", "day_tue",
                  "day_wed", "day_thu", "day_fri", "day_sat"]


KBOARD_BUTTONS_TEXTS = ["◀", KEYBOARD_LOCALE["ok"], "▶", KEYBOARD_LOCALE["monday"], KEYBOARD_LOCALE["tuesday"], KEYBOARD_LOCALE["wednesday"], KEYBOARD_LOCALE["thursday"], KEYBOARD_LOCALE["friday"], KEYBOARD_LOCALE["saturday"]
                        ]
KBOARD_BUTTONS_CALLBACKS = [CallbackData.PrevDay.value, CallbackData.HideDetails.value, CallbackData.NextDay.value, CallbackData.DayPrefix.value+"mon",
                            CallbackData.DayPrefix.value+"tue", CallbackData.DayPrefix.value+"wed", CallbackData.DayPrefix.value+"thu", CallbackData.DayPrefix.value+"fri", CallbackData.DayPrefix.value+"sat"]

buttons = [KeyboardFactory.create_inline_keyboard_button(i[0], i[1]) for i in zip(
    KBOARD_BUTTONS_TEXTS, KBOARD_BUTTONS_CALLBACKS)]
DAY_CHOOSING_KEYBOARD = KeyboardFactory.create_reply_markup(buttons, 3)
