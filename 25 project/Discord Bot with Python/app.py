import discord
import os

# 🔹 Bot ka intent set karna zaroori hai
intents = discord.Intents.default()
intents.messages = True  

# 🔹 Bot ko initialize karna
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ {client.user} is now online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Taake bot apne messages ka reply na de

    if message.content.lower() == "hello":
        await message.channel.send("Hello! How can I help you? 😊")

    if message.content.lower() == "bye":
        await message.channel.send("Goodbye! 👋")

# 🔹 Discord bot token (Replit me environment variable me store karo)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

client.run(TOKEN)
