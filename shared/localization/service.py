from ..logger.logger import logger
from .messages import messages, MessageLocalization
from .keyboards import keyboard_buttons, KeyboardLocalization
from .exceptions import exceptions, ExceptionsLocalization
from shared.services.config import config_service


class LocalizationService:
    def __init__(self, language: str):
        self.language = language
        if not self.is_language_exist(self.language):
            OLD_LANGUAGE = self.language
            self.language = "ru"
            logger.error(f"Language {OLD_LANGUAGE} not found. ")

        logger.init(f"Using language: {self.language}.")

    def get_message(self, key: str) -> str:
        try:
            return messages[self.language][key]
        except:
            return messages["ru"][key]

    def get_keyboard(self, key: str) -> str:
        try:
            return keyboard_buttons[self.language][key]
        except:
            return keyboard_buttons["ru"][key]

    def get_keyboard_dict(self) -> KeyboardLocalization:
        try:
            return keyboard_buttons[self.language]
        except:
            return keyboard_buttons["ru"]

    def get_exceptions_dict(self) -> ExceptionsLocalization:
        try:
            return exceptions[self.language]
        except:
            return exceptions["ru"]

    def get_messages_dict(self) -> MessageLocalization:
        try:
            return messages[self.language]
        except:
            return messages["ru"]

    def is_language_exist(self, language: str) -> bool:
        return language in messages.keys() and language in keyboard_buttons.keys() and language in exceptions.keys()


CURRENT_LANGUAGE = config_service.get("CURRENT_LANGUAGE")
localization_service = LocalizationService(CURRENT_LANGUAGE)
