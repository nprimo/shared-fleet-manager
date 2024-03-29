import discord
import re
import os
from dotenv import load_dotenv
import bot
from host_utils import keep_alive, restart_bot


load_dotenv()
TOKEN = str(os.getenv("DISCORD_TOKEN"))
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

command_prompt = '$'


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    print(message.author, message.channel.id, message.content)
    if message.content.startswith(command_prompt):
        channel = message.channel
        av = re.split(r'\s+', message.content)
        reply = bot.commands(av[0].lower(), message, av)

        await channel.send(reply)


def main():
    keep_alive()
    try:
        client.run(TOKEN)
    except discord.errors.HTTPException:
        restart_bot()


if __name__ == "__main__":
    main()
