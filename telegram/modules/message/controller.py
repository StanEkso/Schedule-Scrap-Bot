from aiogram.types import Message
from shared.services.config import configService


class MessageController:
    SHOULD_DELETE_MESSAGE = configService.get("DELETE_COMMANDS")

    async def deleteMessageIfRequired(self, message: Message):
        if (self.SHOULD_DELETE_MESSAGE):
            try:
                await message.delete()
            except:
                print("[ERROR] Message cannot be deleted")
    pass


messageController = MessageController()
