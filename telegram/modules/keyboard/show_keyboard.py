from aiogram import types
from shared.types.callback import CallbackData
from shared.localization.service import localization_service
from .factory import KeyboardFactory
KEYBOARD_LOCALE = localization_service.get_keyboard_dict()
# Keyboard showed when command /schedule is called

KEYBOARD_TEXTS = [KEYBOARD_LOCALE["show"]]
KEYBOARD_CALLBACKS = [CallbackData.ShowSchedule.value]
buttons = [types.InlineKeyboardButton(i[0], callback_data=i[1]) for i in zip(
    KEYBOARD_TEXTS, KEYBOARD_CALLBACKS)]

SHOW_SCHEDULE_KEYBOARD = KeyboardFactory.createReplyMarkup(buttons, 1)
