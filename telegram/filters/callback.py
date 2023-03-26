from shared.types.callback import CallbackData
from aiogram.types import CallbackQuery


def is_show_schedule(call: CallbackQuery) -> bool:
    return call.data == CallbackData.SHOW_SCHEDULE.value


def is_day(call: CallbackQuery) -> bool:
    return call.data.find(CallbackData.DAY_PREFIX.value) != -1


def is_next_day(call: CallbackQuery) -> bool:
    return call.data == CallbackData.NEXT_DAY.value


def is_prev_day(call: CallbackQuery) -> bool:
    return call.data == CallbackData.PREV_DAY.value


def is_hide(call: CallbackQuery) -> bool:
    return call.data == CallbackData.HIDE_DETAILS.value


def is_close(call: CallbackQuery) -> bool:
    return call.data == CallbackData.CLOSE_SCHEDULE.value


def is_close_exams(call: CallbackQuery) -> bool:
    return call.data == CallbackData.CLOSE_EXAM.value


FILTERS = {
    CallbackData.SHOW_SCHEDULE.value: is_show_schedule,
    CallbackData.DAY_PREFIX.value: is_day,
    CallbackData.NEXT_DAY.value: is_next_day,
    CallbackData.PREV_DAY.value: is_prev_day,
    CallbackData.HIDE_DETAILS.value: is_hide,
    CallbackData.CLOSE_SCHEDULE.value: is_close,
    CallbackData.CLOSE_EXAM.value: is_close_exams
}
