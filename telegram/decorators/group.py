from aiogram.types import ChatType, Message
from shared.localization.service import localization_service
from shared.logger.logger import logger
EXCEPTIONS = localization_service.get_exceptions_dict()


def ChatType(types: list[ChatType] = None, notify_user: bool = False):
    def decorator(func):
        async def wrapper(message: Message, *args, **kwargs):
            if (message.chat.type in types):
                return await func(message, *args, **kwargs)

            logger.error("Incorrect chat type")
            if not notify_user:
                return

            return await message.answer(EXCEPTIONS['INCORRECT_CHAT_TYPE'])
        return wrapper
    return decorator
