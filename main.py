import discord
import logging
import judger
import os
from typing import List

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

class Lang:
    prefix: str
    suffix: str
    uuid: str

    def __init__(self, ext: str, uuid: str):
        self.prefix = "```"+ext
        self.suffix = "```"
        self.uuid = uuid

    async def process(self, msg: discord.Message):
        content: str = msg.content
        if not content.startswith(self.prefix):
            return
        if (not content.endswith(self.suffix)):
            return
        logging.debug("calling remote judger")
        code = content.removeprefix(self.prefix).removesuffix(self.suffix)
        await msg.channel.send("Compiling with "+self.prefix.removeprefix("```")+":\n```c\n"+code+"\n```")
        res = await judger.run(code, "7daff707-26b5-4153-90ae-9858b9fd9619")
        await msg.channel.send("Log:\n```\n"+res.log+"\n```")
        await msg.channel.send("Stdout:\n```\n"+res.stdout+"\n```")

langs: List[Lang] = [Lang("c", "7daff707-26b5-4153-90ae-9858b9fd9619"), Lang(
    "lua", "1c41598f-e253-4f81-9ef5-d50bf1e4e74f"), Lang("cpp", "8a9e1daf-ff89-42c3-b011-bf6fb4bd8b26")]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content: str = message.content
    for lang in langs:
        await lang.process(message)

client.run(os.getenv("TOKEN"))
