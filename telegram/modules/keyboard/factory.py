from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class KeyboardFactory:
    def __init__(self, ):
        pass

    @staticmethod
    def create_reply_markup(keyboard: list[InlineKeyboardButton], rowSize: int = 3) -> InlineKeyboardMarkup:
        returned = InlineKeyboardMarkup()
        for i in range(0, len(keyboard), rowSize):
            returned.add(*keyboard[i:i + rowSize])
            returned.row()

        return returned

    @staticmethod
    def create_inline_keyboard_button(text: str, callbackData: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=text, callback_data=callbackData)

    @staticmethod
    def generate_buttons_from_list(keyboard: list[str], callbackData: str) -> list[InlineKeyboardButton]:
        return [KeyboardFactory.create_inline_keyboard_button(i, callbackData) for i in keyboard]
