from aiogram.types import ChatType, Message
from shared.localization.service import localization_service

EXCEPTIONS = localization_service.get_exceptions_dict()


def ChatType(types: list[ChatType] = None, notifyUser: bool = False):
    def decorator(func):
        async def wrapper(message: Message, *args, **kwargs):
            if (message.chat.type in types):
                return await func(message, *args, **kwargs)
            if not notifyUser:
                return

            return await message.answer(EXCEPTIONS['INCORRECT_CHAT_TYPE'])
        return wrapper
    return decorator
