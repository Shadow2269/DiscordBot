import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from chat import get_bot_response, save_message

# .env laden
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Discord Bot Setup
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot ist eingeloggt als {bot.user}")

@bot.command()
async def chat(ctx, *, message: str):
    await ctx.send("⏳ Denke nach...")
    response = get_bot_response(message)
    save_message(f"User: {message}")
    save_message(f"Bot: {response}")
    await ctx.send(response)

bot.run(TOKEN)

