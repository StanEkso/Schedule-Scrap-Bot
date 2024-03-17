from aiogram import types
from shared.localization.service import localization_service

EXCEPTIONS = localization_service.get_exceptions_dict()


def OnQueryFail(error_text: str = EXCEPTIONS['QUERY_ERROR']):

    def decorator(func):
        async def wrapper(call: types.CallbackQuery, *args, **kwargs):
            try:
                return await func(call=call)
            except Exception as e:
                await call.answer(text=error_text)
                raise e

        return wrapper

    return decorator
