# discord eval

A discord bot to execute message content as code safely

## function

The discord bot check every new message on your discord server, response with result of execution.

![image](https://github.com/Eason0729/discord-eval/assets/30045503/e0abb845-b89f-4c07-8636-05b5dde9a1c6)

![image](https://github.com/Eason0729/discord-eval/assets/30045503/93c1a909-721d-4619-81a2-716c4ced9942)

## Setup

This project rely on mdoj-judger(previously know as modj-sandbox), download judger from [mdoj's github release](https://github.com/mdcpp/mdoj/releases), change config, specifically you want to change the maximum memory reverse for judger, than start the judger.

Then install pip packages with `pip install -r requirements.txt`, set environment variable, finally, start the discord bot.
```
TOKEN=token.of.discord.bot
JUDGER=localhost:8080
```
