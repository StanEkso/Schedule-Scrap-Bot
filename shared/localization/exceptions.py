from typing import TypedDict

ExceptionsLocalization = TypedDict('ExceptionsLocalization', {
    'INCORRECT_CHAT_TYPE': str,
    "ONLY_CURRENT_WEEK": str,
    "QUERY_ERROR": str,
})

exceptions: dict[str, ExceptionsLocalization] = {
    'en': {
        'INCORRECT_CHAT_TYPE': 'This command cannot be used in this chat.',
        "ONLY_CURRENT_WEEK": "⚠️ Only current week lessons are shown.\n",
        "QUERY_ERROR": "Query error. Please, try again later."
    },
    'ru': {
        'INCORRECT_CHAT_TYPE': 'Эта команда не может быть использована в этом чате.',
        "ONLY_CURRENT_WEEK": "⚠️ Показаны только пары текущей недели.\n",
        "QUERY_ERROR": "Ошибка запроса. Пожалуйста, попробуйте позже."
    }
}
