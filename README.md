# Schedule Scrapping Bot

This project is made for convenient way to check schedule of group in telegram instead of visiting web-site.

## Features

- Configurable for any group
- There is an opportunity to easily edit messages
- You can config it with deleting trash messages (commands)
- You can customize command to call bot function

## Stack

- Python
- Aiogram (Telegram Bot API Wrapper)
- BeautifulSoup (HTML Parser)
- Requests (HTTP Client)

## Guide of Deployment

### Pre-Requirements

- You need to use some hosting that allows to use Python
- `[IMPORTNANT]` This repository is ready for use in Heroku

### Deployment (Heroku Example)

- Fork this repository
- Connect forked repository in Heroku Application
- Set Environment Variables `TOKEN`, `COURSE` and `GROUP`, where `TOKEN` is given by [Bot Father](!https://t.me/BotFather).
- Invite created bot in your group or use it in private messages

## Local Development

- Fork this repository and clone it on your device
- Check out `requirements.txt` with deps.
- Change `.dev.env.example` to `.dev.env` and pass `TOKEN`, `COURSE` and `GROUP` vars.
- Now bot is ready for local development
- Run `python bot.py` to run bot instance.

## Configuration

Project offer a lot of opportunities to customize it for your needs.

### Shared configuration

#### **~/settings.json**

`DELETE_COMMANDS` - if `true` bot will delete commands after execution (of course if bot has permissions to do it)

`WRITE_LOGS` - if `true` bot will write logs in terminal.

`CURRENT_LANGUAGE` - check [Localization](#localization) section for more info.

#### **ENV Variables**

`TOKEN` - token of your bot, given by [Bot Father](!https://t.me/BotFather).

`COURSE` - course of your group.

`GROUP` - number of your group.

### Schedule module

#### **~/settings.json**

`UPDATE_ON_EVERY_SHOW` - if `true` bot will update schedule on every show command.

`SCHEDULE_COMMANDS` - commands to call schedule module.

#### **ENV Variables**

`COURSE` - course of your group.

`GROUP` - number of your group.

### Exams module

#### **~/settings.json**

`EXAMS_COMMANDS` - commands to call exams module.

#### **ENV Variables**

`COURSE` - course of your group.

`GROUP` - number of your group.

### Localization

#### **~/settings.json**

`CURRENT_LANGUAGE` - current language of bot.

#### **Python files**

Messages, exceptions and keyboard texts can be changed in `shared/localization` folder.

- `messages.py` - messages
- `exceptions.py` - exceptions
- `keyboards.py` - keyboard texts

For example, localization for exceptions

```python
ExceptionsLocalization = TypedDict('ExceptionsLocalization', {
    'INCORRECT_CHAT_TYPE': str,
    "ONLY_CURRENT_WEEK": str,
    "QUERY_ERROR": str,
})


'en': {
        'INCORRECT_CHAT_TYPE': 'This command cannot be used in this chat.',
        "ONLY_CURRENT_WEEK": "⚠️ Only current week lessons are shown.\n",
        "QUERY_ERROR": "Query error. Please, try again later."
}

```
