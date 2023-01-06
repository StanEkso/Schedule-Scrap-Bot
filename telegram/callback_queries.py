from aiogram import types
from .decorators.logger import LogCall
from shared.localization.service import localization
from .filters.callback import isCloseCallback, isDayCallback, isHideCallback, isNextDayCallback, isPrevDayCallback, isShowScheduleCallback
from .decorators.failquery import OnQueryFail
from .modules.schedule.controller import scheduleController
from .__init__ import dp


def init():

    @dp.callback_query_handler(isShowScheduleCallback)
    @LogCall(SHOW_CHAT_TYPE=True)
    async def handleShowSchedule(call: types.CallbackQuery, *args, **kwargs):
        return await scheduleController.showSchedule(call.message)

    # Bot handle callback query "day_{wd}"

    @dp.callback_query_handler(isDayCallback)
    @OnQueryFail(localization.getMessage("day_is_chosen"))
    @LogCall(SHOW_CHAT_TYPE=True)
    async def handleShowSchedule(call: types.CallbackQuery, *args, **kwargs):
        return await scheduleController.editSchedule(call.message, call.data)

    # Bot handle callback query "next_day"

    @dp.callback_query_handler(isNextDayCallback)
    @LogCall(SHOW_CHAT_TYPE=True)
    async def handleNextDaySchedule(call: types.CallbackQuery, *args, **kwargs):
        return await scheduleController.sendNextDaySchedule(call.message)

    # Bot handle callback query "prev_day"

    @dp.callback_query_handler(isPrevDayCallback)
    @LogCall(SHOW_CHAT_TYPE=True)
    async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
        return await scheduleController.sendPrevDaySchedule(call.message)

    # Bot handle callback query "hide_details"

    @dp.callback_query_handler(isHideCallback)
    @LogCall(SHOW_CHAT_TYPE=True)
    async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
        return await scheduleController.hideSchedule(call.message)

    # Bot handle callback query "close_schedule"

    @dp.callback_query_handler(isCloseCallback)
    @LogCall(SHOW_CHAT_TYPE=True)
    async def handlePrevDaySchedule(call: types.CallbackQuery, *args, **kwargs):
        return await scheduleController.deleteScheduleMessage(call.message)
