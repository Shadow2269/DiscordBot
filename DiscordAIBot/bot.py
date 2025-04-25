# bot.py
import discord
from config import DISCORD_TOKEN
from discord.ext import commands
from config import OWNER_ID
from persona_handler import save_persona, load_persona
from chat import ask_gpt
#from music_handler import play_music  # Import play_music if it exists in music_handler

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!",intents=intents)

# globale Variable laden
current_persona = load_persona()

@bot.command()
async def persona(ctx, *, style):
    if ctx.author.id != OWNER_ID:
        await ctx.send("Nur der Owner darf meine Persönlichkeit ändern. 🔒")
        return

    save_persona(style.lower())
    await ctx.send(f"Charakter geändert zu: `{style.lower()}` 🧠")

@bot.command()
async def whoami(ctx):
    style = load_persona()
    await ctx.send(f"Aktuelle Persönlichkeit: `{style}`")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command()
async def chat(ctx, *, message):
    response = await ask_gpt(message, ctx.author.id)
    await ctx.send(response)


@bot.command()
async def join(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("Bin im Voice!")
    else:
        await ctx.send("Du bist nicht in einem Voice-Channel.")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Bin raus.")
    else:
        await ctx.send("Ich bin gar nicht drin.")

#@bot.command()
#async def play(ctx, url):
#    if ctx.voice_client:
#        await play_music(ctx, url)  # Ensure play_music is defined or imported
#        await ctx.send("Spiele Musik.")
#   else:
#        await ctx.send("Ich bin nicht im Voice. Nutze !join.")

bot.run(DISCORD_TOKEN)
