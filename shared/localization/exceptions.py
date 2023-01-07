# Create a typing for exceptions localization inherits from TypedDict

from typing import TypedDict

ExceptionsLocalization = TypedDict('ExceptionsLocalization', {
    'INCORRECT_CHAT_TYPE': str,
})

exceptions: dict[str, ExceptionsLocalization] = {
    'en': {
        'INCORRECT_CHAT_TYPE': 'This command cannot be used in this chat.',
    },
    'ru': {
        'INCORRECT_CHAT_TYPE': 'Эта команда не может быть использована в этом чате.',
    }
}
