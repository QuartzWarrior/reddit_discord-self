import discord
from discord.ext import tasks

client = discord.Client()

channel_ids = [123456789012345678, 987654321098765432] # channel ids

message_content = "hello" # message you want

interval = 60 # minutes

@tasks.loop(minutes=interval)
async def send_message():
    for channel_id in channel_ids:
        channel = client.get_channel(channel_id)
        if channel:
            await channel.send(message_content)
        else:
            print(f"Failed to find channel with ID {channel_id}")

@send_message.before_loop
async def before():
    await client.wait_until_ready()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

if __name__ == "__main__":
    send_message.start()
    client.run("TOKEN")