# Create a localization service that will return the correct localization for the current language using messages.py and keyboards.py
from .messages import messages
from .keyboards import keyboard_buttons, KeyboardLocalization
from .exceptions import exceptions, ExceptionsLocalization
from shared.services.config import configService


class LocalizationService:
    def __init__(self, language: str):
        self.language = language
        try:
            messages[self.language]
        except:
            self.language = "ru"
            print("Language not found, using default: " + self.language)

    def getMessage(self, key: str) -> str:
        try:
            return messages[self.language][key]
        except:
            return messages["ru"][key]

    def getKeyboard(self, key: str) -> str:
        try:
            return keyboard_buttons[self.language][key]
        except:
            return keyboard_buttons["ru"][key]

    def getRawKeyboard(self) -> KeyboardLocalization:
        try:
            return keyboard_buttons[self.language]
        except:
            return keyboard_buttons["ru"]

    def getRawExceptions(self) -> ExceptionsLocalization:
        try:
            return exceptions[self.language]
        except:
            return exceptions["ru"]


localization = LocalizationService(configService.get("CURRENT_LANGUAGE"))
