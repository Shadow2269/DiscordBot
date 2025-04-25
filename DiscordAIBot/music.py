# music.py
import discord
from discord.ext import commands
import yt_dlp

ydl_opts = {
    'format': 'bestaudio',
    'noplaylist': True,
    'quiet': True,
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

async def play_music(ctx, url):
    vc = ctx.voice_client

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']

    vc.stop()
    vc.play(discord.FFmpegPCMAudio(audio_url), after=lambda e: print('done', e))
