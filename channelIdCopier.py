import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    await save_channel_ids()

async def save_channel_ids():
    channel_ids = []
    for guild in client.guilds:
        for channel in guild.text_channels:
            permissions = channel.permissions_for(guild.me)
            if permissions.send_messages:
                channel_ids.append(str(channel.id))

    with open('channel_ids.txt', 'w') as file:
        file.write('\n'.join(channel_ids))

    print('Channel IDs saved to channel_ids.txt')

client.run('YOUR_TOKEN')