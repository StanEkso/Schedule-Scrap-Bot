from aiogram.types import Message, CallbackQuery
from shared.services.config import configService
WRITE_LOGS = not not configService.get("WRITE_LOGS") or False


def LogMessage(SHOW_TIME: bool = False, SHOW_CHAT_TYPE: bool = False):
    def decorator(func):
        if (not WRITE_LOGS):
            return func

        async def wrapper(message: Message = None, *args, **kwargs):
            LOG_MESSAGE = messageToString(message)

            if SHOW_CHAT_TYPE:
                LOG_MESSAGE = messageToChatType(message) + " " + LOG_MESSAGE

            if SHOW_TIME:
                LOG_MESSAGE = messageToSentTime(message) + " " + LOG_MESSAGE

            print(LOG_MESSAGE)
            return await func(message=message, *args, **kwargs)
        return wrapper
    return decorator


def LogCall(SHOW_CHAT_TYPE: bool = False):
    def decorator(func):
        if (not WRITE_LOGS):
            return func

        async def wrapper(call: CallbackQuery = None, *args, **kwargs):
            LOG_MESSAGE = callToString(call)

            if SHOW_CHAT_TYPE:
                LOG_MESSAGE = callToChatType(call) + " " + LOG_MESSAGE

            print(LOG_MESSAGE)
            return await func(call=call, *args, **kwargs)
        return wrapper
    return decorator

# Write a function taking message and returning a string in format:
# "Firstname Lastname (@username) sent a message: message_text"
#


def messageToString(message: Message) -> str:
    FIRST_NAME = message.from_user.first_name or ""
    LAST_NAME = message.from_user.last_name or ""
    USERNAME = message.from_user.username or ""
    TEXT = message.text or ""
    return f"{FIRST_NAME} {LAST_NAME} (@{USERNAME}) sent a message: {TEXT}"


def callToString(call: CallbackQuery) -> str:
    FIRST_NAME = call.from_user.first_name or ""
    LAST_NAME = call.from_user.last_name or ""
    USERNAME = call.from_user.username or ""
    DATA = call.data or ""
    return f"{FIRST_NAME} {LAST_NAME} (@{USERNAME}) sent a callback: {DATA}"


def callToChatType(call: CallbackQuery) -> str:
    return f"[{call.message.chat.type.upper()}]"


def messageToSentTime(message: Message) -> str:
    return f"[{message.date.strftime('%H:%M:%S')}]"


def messageToChatType(message: Message) -> str:
    return f"[{message.chat.type.upper()}]"
