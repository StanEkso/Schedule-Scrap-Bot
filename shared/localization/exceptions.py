# Create a typing for exceptions localization inherits from TypedDict

from typing import TypedDict

ExceptionsLocalization = TypedDict('ExceptionsLocalization', {
    'INCORRECT_CHAT_TYPE': str,
    "ONLY_CURRENT_WEEK": str
})

exceptions: dict[str, ExceptionsLocalization] = {
    'en': {
        'INCORRECT_CHAT_TYPE': 'This command cannot be used in this chat.',
        "ONLY_CURRENT_WEEK": "⚠️ Only current week lessons are shown.\n"
    },
    'ru': {
        'INCORRECT_CHAT_TYPE': 'Эта команда не может быть использована в этом чате.',
        "ONLY_CURRENT_WEEK": "⚠️ Показаны только пары текущей недели.\n"
    }
}
