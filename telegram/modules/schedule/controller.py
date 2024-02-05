from aiogram.types import Message
from ..keyboard.show_keyboard import SHOW_SCHEDULE_KEYBOARD
from ..keyboard.day_keyboard import DAY_CHOOSING_KEYBOARD, DAYS_CALLBACKS
from ..keyboard.close_keyboard import CLOSE_SCHEDULE_KEYBOARD
from shared.localization.service import localization_service
from .service import scheduleService
from shared.services.config import config_service
from shared.structures.hash import IntegerHash

from ..message.controller import messageController


def messageToId(message: Message) -> str:
    return str(message.chat.id) + "_" + str(message.message_id)

hash = IntegerHash()

class ScheduleController:
    async def showEnterMessage(self, message: Message):
        await message.answer(text=localization_service.get_message("show"), reply_markup=SHOW_SCHEDULE_KEYBOARD)
        await messageController.delete_message_if_required(message)

    async def editSchedule(self, message: Message, day: str):
        INDEX = DAYS_CALLBACKS.index(day)

        hash.set(key=messageToId(message), value=INDEX)

        await message.edit_text(text=scheduleService.atDay(INDEX), reply_markup=DAY_CHOOSING_KEYBOARD)

    async def showSchedule(self, message: Message):
        if (config_service.get("UPDATE_ON_EVERY_SHOW") == True):
            await scheduleService.update()

        INDEX = hash.get(key=messageToId(message)) or 0

        if (self.isNewMessage(message)):
            # TODO: remove deadlock here
            await scheduleService.update()
        await message.edit_text(text=scheduleService.atDay(INDEX), reply_markup=DAY_CHOOSING_KEYBOARD)

        hash.set(messageToId(message), INDEX)

    async def sendNextDaySchedule(self, message: Message):
        INDEX = hash.get(key=messageToId(message)) or 0
        NEW_INDEX = self.getNewIndex(INDEX, 1)
        try:
            await message.edit_text(text=scheduleService.atDay(NEW_INDEX), reply_markup=DAY_CHOOSING_KEYBOARD)
        except Exception as e:
            raise e
        finally:
            hash.set(key=messageToId(message), value=NEW_INDEX)

    async def sendPrevDaySchedule(self, message: Message):
        INDEX = hash.get(key=messageToId(message)) or 0
        NEW_INDEX = self.getNewIndex(INDEX, -1)

        try:
            await message.edit_text(text=scheduleService.atDay(NEW_INDEX), reply_markup=DAY_CHOOSING_KEYBOARD)
        except Exception as e:
            raise e
        finally:
            hash.set(key=messageToId(message), value=NEW_INDEX)

    async def hideSchedule(self, message: Message):
        await message.edit_text(text=localization_service.get_message("schedule_closed"), reply_markup=CLOSE_SCHEDULE_KEYBOARD)

    async def deleteScheduleMessage(self, message: Message):
        await message.delete()

    @staticmethod
    def getNewIndex(index: int, direction: int = 1) -> int:
        # 0 - monday, 1 - tuesday, 2 - wednesday, 3 - thursday, 4 - friday, 5 - saturday
        if (index + direction > 5):
            return 0
        elif (index + direction < 0):
            return 5
        return index + direction

    @staticmethod
    def isNewMessage(message: Message) -> bool:
        if (hash.get(key=messageToId(message)) is None):
            return True
        return False


scheduleController = ScheduleController()
