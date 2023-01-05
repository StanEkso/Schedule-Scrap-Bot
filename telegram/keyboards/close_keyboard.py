from shared.types.callback import CallbackData
from shared.localization.service import localization
from telegram.keyboards.factory import KeyboardFactory
KEYBOARD_LOCALE = localization.getRawKeyboard()

KEYBOARDS_TEXTS = [KEYBOARD_LOCALE["show"], KEYBOARD_LOCALE["close"]]
KEYBOARDS_CALLBACKS = [CallbackData.SHOW_SCHEDULE.value,
                       CallbackData.CLOSE_SCHEDULE.value]

buttons = [KeyboardFactory.createInlineKeyboardButton(i[0], i[1]) for i in zip(
    KEYBOARDS_TEXTS, KEYBOARDS_CALLBACKS)]
CLOSE_SCHEDULE_KEYBOARD = KeyboardFactory.createReplyMarkup(buttons, 1)
