# Assign lambda function to variable

from shared.types.callback import CallbackData
from aiogram.types import CallbackQuery


def isShowScheduleCallback(call: CallbackQuery) -> bool:
    return call.data == CallbackData.SHOW_SCHEDULE.value


def isDayCallback(call: CallbackQuery) -> bool:
    return call.data.find(CallbackData.DAY_PREFIX.value) != -1


def isNextDayCallback(call: CallbackQuery) -> bool:
    return call.data == CallbackData.NEXT_DAY.value


def isPrevDayCallback(call: CallbackQuery) -> bool:
    return call.data == CallbackData.PREV_DAY.value


def isHideCallback(call: CallbackQuery) -> bool:
    return call.data == CallbackData.HIDE_DETAILS.value


def isCloseCallback(call: CallbackQuery) -> bool:
    return call.data == CallbackData.CLOSE_SCHEDULE.value