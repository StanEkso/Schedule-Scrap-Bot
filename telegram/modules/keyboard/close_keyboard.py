from shared.types.callback import CallbackData
from shared.localization.service import localization_service
from .factory import KeyboardFactory
KEYBOARD_LOCALE = localization_service.get_keyboard_dict()

KEYBOARDS_TEXTS = [KEYBOARD_LOCALE["show"], KEYBOARD_LOCALE["close"]]
KEYBOARDS_CALLBACKS = [CallbackData.ShowSchedule.value,
                       CallbackData.CloseSchedule.value]

buttons = [KeyboardFactory.create_inline_keyboard_button(i[0], i[1]) for i in zip(
    KEYBOARDS_TEXTS, KEYBOARDS_CALLBACKS)]
CLOSE_SCHEDULE_KEYBOARD = KeyboardFactory.create_reply_markup(buttons, 1)
