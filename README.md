# Schedule Scrapping Bot

This project is made for convenient way to check schedule of group in telegram instead of visiting web-site.

## Features

- Configurable for any group
- There is an opportunity to easily edit messages
- You can config it with deleting trash messages (commands)
- You can customize command to call bot function

## Guide of Deployment

### Pre-Requirements

- You need to use some hosting that allows to use Python
- This repository is ready for use in Heroku

### Deployment (Heroku Example)

- Fork this repository
- Connect forked repository in Heroku Application
- Set Environment Variables `TOKEN` and `PARSE_URL`, where `TOKEN` is given by [Bot Father](!https://t.me/BotFather).
- Invite created bot in your group or use it in private messages
- `Optional` If you want bot to delete commands in groups, it need him to get `can_delete_messages` permission.

## Local Development

- Fork this repository and clone it on your device
- Check out `requirements.txt` with deps.
- Change `.dev.env.example` to `.dev.env` and pass `TOKEN` and `PARSE_URL` vars.
- Now bot is ready for local development
- Run `python bot.py` to run bot instance.
