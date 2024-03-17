from aiogram.types import Message, CallbackQuery
from shared.helpers.helpers import to_non_empty
from shared.services.config import config_service
from shared.logger.logger import logger
WRITE_LOGS = not not config_service.get("WRITE_LOGS") or False


def LogMessage(show_time: bool = False, show_chat_type: bool = False):
    def decorator(func):
        if (not WRITE_LOGS):
            return func

        async def wrapper(message: Message = None, *args, **kwargs):
            logged_message = convert_message(message)

            if show_chat_type:
                logged_message = convert_message_to_chat_type(
                    message) + " " + logged_message

            if show_time:
                logged_message = convert_message_to_sent_time(
                    message) + " " + logged_message

            logger.custom(logged_message, "MESSAGE")

            return await func(message=message, *args, **kwargs)
        return wrapper
    return decorator


def LogCall(show_chat_type: bool = False):
    def decorator(func):
        if (not WRITE_LOGS):
            return func

        async def wrapper(call: CallbackQuery = None, *args, **kwargs):
            logged_message = convert_call(call)

            if show_chat_type:
                logged_message = convert_call_to_chat_type(
                    call) + " " + logged_message

            logger.custom(logged_message, "QUERY")

            return await func(call=call, *args, **kwargs)
        return wrapper
    return decorator


def convert_message(message: Message) -> str:
    first_name = message.from_user.first_name or ""
    last_name = message.from_user.last_name or ""
    username = message.from_user.username or ""
    username = f"(@{username})" if len(username) > 0 else ""
    text = message.text or ""

    return " ".join(to_non_empty([first_name, last_name, username, "sent:", text]))


def convert_call(call: CallbackQuery) -> str:
    first_name = call.from_user.first_name or ""
    last_name = call.from_user.last_name or ""
    username = call.from_user.username or ""
    username = f"(@{username})" if len(username) > 0 else ""
    data = call.data or ""
    return " ".join(to_non_empty([first_name, last_name, username, "sent:", data]))


def convert_call_to_chat_type(call: CallbackQuery) -> str:
    return f"[{call.message.chat.type.upper()}]"


def convert_message_to_sent_time(message: Message) -> str:
    return f"[{message.date.strftime('%H:%M:%S')}]"


def convert_message_to_chat_type(message: Message) -> str:
    return f"[{message.chat.type.upper()}]"
