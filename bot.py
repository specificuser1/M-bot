import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

with open("config.json") as f:
    config = json.load(f)

queues = {}

# --------------------------------------
# MUSIC COMMANDS
# --------------------------------------
@bot.event
async def on_ready():
    print(f"{bot.user} is online in guild {GUILD_ID}!")

async def ensure_voice(ctx):
    if ctx.author.voice is None:
        await ctx.send("Please join a voice channel first!")
        return False
    if ctx.voice_client is None:
        await ctx.author.voice.channel.connect()
    return True

@bot.command()
async def play(ctx, *, url):
    if not await ensure_voice(ctx):
        return

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    voice = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['url']
        source = FFmpegPCMAudio(url2, **FFMPEG_OPTIONS)
        if not voice.is_playing():
            voice.play(source, after=lambda e: print('done', e))
            await ctx.send(f"Playing: {info['title']}")
        else:
            if ctx.guild.id not in queues:
                queues[ctx.guild.id] = []
            queues[ctx.guild.id].append(source)
            await ctx.send(f"Queued: {info['title']}")

@bot.command()
async def skip(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("Skipped the current song!")

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel.")

@bot.command()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("Paused the song!")

@bot.command()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Resumed the song!")

bot.run(TOKEN)
