from typing import TypedDict


# Create a typing for keyboard localization inherits from TypedDict
KeyboardLocalization = TypedDict('KeyboardLocalization', {
    'show': str,
    'close': str,
    'monday': str,
    'tuesday': str,
    'wednesday': str,
    'thursday': str,
    'friday': str,
    'saturday': str,
    "ok": str
})

keyboard_buttons: dict[str, KeyboardLocalization] = {
    "ru": {
        'show': 'Показать расписание',
        'close': 'Закрыть расписание',
        'monday': 'ПН',
        'tuesday': 'ВТ',
        'wednesday': 'СР',
        'thursday': 'ЧТ',
        'friday': 'ПТ',
        'saturday': 'СБ',
        "ok": "OK"
    },
    # Create another language localization English
    "en": {
        'show': 'Show schedule',
        'close': 'Close schedule',
        'monday': 'MO',
        'tuesday': 'TU',
        'wednesday': 'WE',
        'thursday': 'TH',
        'friday': 'FR',
        'saturday': 'SA',
        "ok": "OK"
    }
}
