from aiogram.types import Message, CallbackQuery
from shared.services.config import config_service
from shared.logger.logger import logger
WRITE_LOGS = not not config_service.get("WRITE_LOGS") or False


def LogMessage(SHOW_TIME: bool = False, show_chat_type: bool = False):
    def decorator(func):
        if (not WRITE_LOGS):
            return func

        async def wrapper(message: Message = None, *args, **kwargs):
            LOG_MESSAGE = convert_message(message)

            if show_chat_type:
                LOG_MESSAGE = convert_message_to_chat_type(
                    message) + " " + LOG_MESSAGE

            if SHOW_TIME:
                LOG_MESSAGE = convert_message_to_sent_time(
                    message) + " " + LOG_MESSAGE

            logger.custom(LOG_MESSAGE, "MESSAGE")

            return await func(message=message, *args, **kwargs)
        return wrapper
    return decorator


def LogCall(SHOW_CHAT_TYPE: bool = False):
    def decorator(func):
        if (not WRITE_LOGS):
            return func

        async def wrapper(call: CallbackQuery = None, *args, **kwargs):
            LOG_MESSAGE = convert_call(call)

            if SHOW_CHAT_TYPE:
                LOG_MESSAGE = convert_call_to_chat_type(
                    call) + " " + LOG_MESSAGE

            logger.custom(LOG_MESSAGE, "QUERY")

            return await func(call=call, *args, **kwargs)
        return wrapper
    return decorator


def convert_message(message: Message) -> str:
    FIRST_NAME = message.from_user.first_name or ""
    LAST_NAME = message.from_user.last_name or ""
    USERNAME = message.from_user.username or ""
    TEXT = message.text or ""
    return f"{FIRST_NAME} {LAST_NAME} (@{USERNAME}) sent: {TEXT}"


def convert_call(call: CallbackQuery) -> str:
    FIRST_NAME = call.from_user.first_name or ""
    LAST_NAME = call.from_user.last_name or ""
    USERNAME = call.from_user.username or ""
    DATA = call.data or ""
    return f"{FIRST_NAME} {LAST_NAME} (@{USERNAME}) sent: {DATA}"


def convert_call_to_chat_type(call: CallbackQuery) -> str:
    return f"[{call.message.chat.type.upper()}]"


def convert_message_to_sent_time(message: Message) -> str:
    return f"[{message.date.strftime('%H:%M:%S')}]"


def convert_message_to_chat_type(message: Message) -> str:
    return f"[{message.chat.type.upper()}]"
