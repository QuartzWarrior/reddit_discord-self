import os
import random
import discord
from discord.ext import tasks
    
client = discord.Client()
    
target_user_id = "00000000"
    
@tasks.loop(minutes=10)
async def send_random_image():
    folder_path = "folders/"
    image_files = [f for f in os.listdir(folder_path) if f.endswith((".jpg", ".jpeg", ".png", ".gif"))]
    
    if image_files:
        random_image = random.choice(image_files)
        image_path = os.path.join(folder_path, random_image)
    
        target_user = await client.fetch_user(target_user_id)
        if target_user:
            try:
                with open(image_path, "rb") as f:
                    await target_user.send(file=discord.File(f))
                print(f"Sent image {random_image} to user {target_user_id}")
            except discord.Forbidden:
                print(f"Unable to send DM to user {target_user_id}. DM permissions may be disabled.")
        else:
            print(f"User {target_user_id} not found.")
    else:
        print("No image files found in the 'folders/' directory.")
    
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    send_random_image.start()
    
client.run("TOKEN")