import discord
from discord.ext import tasks

CHANNEL_ID = 000000
INVITE = 'INVITE_LINK'

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    messager.start()

@tasks.loop(hours=6)
async def messager():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"Hey, my guild is recruiting new members! If you're interested, join our Discord server: {INVITE}")
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send(f"If you have any questions, just join the Discord server and ask there: {INVITE}")

client.run("TOKEN")