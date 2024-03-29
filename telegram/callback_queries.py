from aiogram import types
from .decorators.logger import LogCall
from shared.localization.service import localization_service
from .filters.callback import FILTERS as CALLBACK
from .decorators.failquery import OnQueryFail
from .modules.schedule.controller import scheduleController
from .modules.exam.controller import exam_controller
from .__init__ import dp


@LogCall(show_chat_type=True)
async def handleShowSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.showSchedule(call.message)


@OnQueryFail(localization_service.get_message("day_is_chosen"))
@LogCall(show_chat_type=True)
async def handleEditSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.editSchedule(call.message, call.data)


@LogCall(show_chat_type=True)
async def handleNextDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.sendNextDaySchedule(call.message)


@LogCall(show_chat_type=True)
async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.sendPrevDaySchedule(call.message)


@LogCall(show_chat_type=True)
async def handleHideSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.hideSchedule(call.message)


@LogCall(show_chat_type=True)
async def handleDeleteScheduleMessage(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.deleteScheduleMessage(call.message)


@LogCall(show_chat_type=True)
async def handleDeleteExamMessage(call: types.CallbackQuery, *args, **kwargs):
    return await exam_controller.close_exam_message(call.message)


def init():
    dp.register_callback_query_handler(
        handleShowSchedule, CALLBACK["show_schedule"])

    dp.register_callback_query_handler(
        handleEditSchedule, CALLBACK["day_"])

    dp.register_callback_query_handler(
        handleNextDaySchedule, CALLBACK["next_day"])

    dp.register_callback_query_handler(
        handlePrevDaySchedule, CALLBACK["prev_day"])

    dp.register_callback_query_handler(
        handleHideSchedule, CALLBACK["hide_details"])

    dp.register_callback_query_handler(
        handleDeleteScheduleMessage, CALLBACK["close_schedule"])

    dp.register_callback_query_handler(
        handleDeleteExamMessage, CALLBACK["close_exam"])
