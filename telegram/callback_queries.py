from aiogram import types
from .decorators.logger import LogCall
from shared.localization.service import localization
from .filters.callback import isCloseCallback, isDayCallback, isHideCallback, isNextDayCallback, isPrevDayCallback, isShowScheduleCallback
from .decorators.failquery import OnQueryFail
from .modules.schedule.controller import scheduleController
from .modules.exam.controller import examController
from .__init__ import dp


@LogCall(SHOW_CHAT_TYPE=True)
async def handleShowSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.showSchedule(call.message)


@OnQueryFail(localization.getMessage("day_is_chosen"))
@LogCall(SHOW_CHAT_TYPE=True)
async def handleEditSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.editSchedule(call.message, call.data)


@LogCall(SHOW_CHAT_TYPE=True)
async def handleNextDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.sendNextDaySchedule(call.message)


@LogCall(SHOW_CHAT_TYPE=True)
async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.sendPrevDaySchedule(call.message)


@LogCall(SHOW_CHAT_TYPE=True)
async def handleHideSchedule(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.hideSchedule(call.message)


@LogCall(SHOW_CHAT_TYPE=True)
async def handleDeleteScheduleMessage(call: types.CallbackQuery, *args, **kwargs):
    return await scheduleController.deleteScheduleMessage(call.message)


@LogCall(SHOW_CHAT_TYPE=True)
async def handleDeleteExamMessage(call: types.CallbackQuery, *args, **kwargs):
    return await examController.closeExamMessage(call.message)


def init():
    dp.register_callback_query_handler(
        handleShowSchedule, isShowScheduleCallback)

    dp.register_callback_query_handler(
        handleEditSchedule, isDayCallback)

    dp.register_callback_query_handler(
        handleNextDaySchedule, isNextDayCallback)

    dp.register_callback_query_handler(
        handlePrevDaySchedule, isPrevDayCallback)

    dp.register_callback_query_handler(
        handleHideSchedule, isHideCallback)

    dp.register_callback_query_handler(
        handleDeleteScheduleMessage, isCloseCallback)

    dp.register_callback_query_handler(
        handleDeleteExamMessage, lambda call: call.data == "close_exam")
