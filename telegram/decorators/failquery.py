# Create a decorator with arguments that will be used for catching errors in the functions.

from aiogram import types


def OnQueryFail(error_text: str = "Произошла ошибка, попробуйте позже"):

    def decorator(func):

        async def wrapper(call: types.CallbackQuery, *args, **kwargs):
            try:
                return await func(call=call)
            except Exception as e:
                await call.answer(text=error_text)
                raise e
        return wrapper
    return decorator
