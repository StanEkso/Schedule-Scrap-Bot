from .messages import messages
from .keyboards import keyboard_buttons, KeyboardLocalization
from .exceptions import exceptions, ExceptionsLocalization
from shared.services.config import configService


class LocalizationService:
    def __init__(self, language: str):
        self.language = language
        if not self.isLanguageExists(self.language):
            OLD_LANGUAGE = self.language
            self.language = "ru"
            print(
                f"[ERROR] Language {OLD_LANGUAGE} not found.")

        print(f"[INIT] Using language: {self.language}.")

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

    def isLanguageExists(self, language: str) -> bool:
        return language in messages.keys() and language in keyboard_buttons.keys() and language in exceptions.keys()


localization = LocalizationService(configService.get("CURRENT_LANGUAGE"))
