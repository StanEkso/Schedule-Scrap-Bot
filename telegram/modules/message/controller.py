from aiogram.types import Message
from shared.services.config import configService
from shared.logger.logger import logger


class MessageController:
    """
    Base utility class for message handling

    Parameter "DELETE_COMMANDS" in settings.json is determines.
    """
    SHOULD_DELETE_MESSAGE = configService.get("DELETE_COMMANDS")

    async def deleteMessageIfRequired(self, message: Message):
        if (self.SHOULD_DELETE_MESSAGE):
            try:
                await message.delete()
            except:
                logger.error("Message cannot be deleted")


messageController = MessageController()
