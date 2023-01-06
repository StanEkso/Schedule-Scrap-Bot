from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class KeyboardFactory:
    def __init__(self, ):
        pass

    @staticmethod
    def createReplyMarkup(keyboard: list[InlineKeyboardButton], rowSize: int = 3) -> InlineKeyboardMarkup:
        returned = InlineKeyboardMarkup()
        for i in range(0, len(keyboard), rowSize):
            returned.add(*keyboard[i:i + rowSize])
            returned.row()

        return returned

    @staticmethod
    def createInlineKeyboardButton(text: str, callbackData: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callbackData)

    @staticmethod
    def generateButtonsFromList(keyboard: list[str], callbackData: str) -> list[InlineKeyboardButton]:
        return [KeyboardFactory.createInlineKeyboardButton(i, callbackData) for i in keyboard]
