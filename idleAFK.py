import discord
from discord.ext import tasks
from datetime import datetime, timedelta

client = discord.Client()

last_message_time = None

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    check_idle.start()

@client.event
async def on_message(message):
    global last_message_time
    if message.author == client.user:
        last_message_time = datetime.now()
        await client.change_presence(status=discord.Status.online)

@tasks.loop(minutes=1)
async def check_idle():
    global last_message_time
    if last_message_time is not None:
        idle_time = timedelta(minutes=30)
        if datetime.now() - last_message_time >= idle_time:
            await client.change_presence(status=discord.Status.idle)


client.run('TOKEN')