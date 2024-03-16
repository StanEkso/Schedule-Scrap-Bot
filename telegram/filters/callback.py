from shared.types.callback import CallbackData
from aiogram.types import CallbackQuery


def is_show_schedule(call: CallbackQuery) -> bool:
    return call.data == CallbackData.ShowSchedule.value


def is_day(call: CallbackQuery) -> bool:
    return call.data.find(CallbackData.DayPrefix.value) != -1


def is_next_day(call: CallbackQuery) -> bool:
    return call.data == CallbackData.NextDay.value


def is_prev_day(call: CallbackQuery) -> bool:
    return call.data == CallbackData.PrevDay.value


def is_hide(call: CallbackQuery) -> bool:
    return call.data == CallbackData.HideDetails.value


def is_close(call: CallbackQuery) -> bool:
    return call.data == CallbackData.CloseSchedule.value


def is_close_exams(call: CallbackQuery) -> bool:
    return call.data == CallbackData.CloseExam.value


FILTERS = {
    CallbackData.ShowSchedule.value: is_show_schedule,
    CallbackData.DayPrefix.value: is_day,
    CallbackData.NextDay.value: is_next_day,
    CallbackData.PrevDay.value: is_prev_day,
    CallbackData.HideDetails.value: is_hide,
    CallbackData.CloseSchedule.value: is_close,
    CallbackData.CloseExam.value: is_close_exams
}
