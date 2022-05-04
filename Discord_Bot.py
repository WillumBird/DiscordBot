from __future__ import unicode_literals
import discord
import os
import requests
import time
import random
import re,subprocess,urllib.parse,urllib.request
import pafy
from discord.ext import tasks, commands
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.voice_client import VoiceClient
import ffmpeg
import nacl
import youtube_dl
import glob
import asyncio
from asyncio import sleep
#command prefix
client = commands.Bot(command_prefix = '.')


#bot key
TOKEN = ''


#prints out that the bot is online
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  

#command for list of mp3's
@client.command(pass_context=True)
async def jukebox(ctx):
    await message.channel.send(glob.glob("*.mp3"))


#command for bot to join
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command(pass_context=True)
async def test(ctx):
    await message.channel.send("commands work")


#command to play queue
@client.command(pass_context=True)
async def play(ctx):
    voice_channel = ctx.author.voice.channel
    channel = voice_channel.name
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="haHa.mp3"))
    while vc.is_playing():
        await sleep(4)
    await vc.disconnect()

#command to download from YouTube
@client.command(pass_context=True)
async def download(ctx,name):
    query_string = urllib.parse.urlencode({"search_query":name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2="https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    print(clip2)
    ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([clip2])


#run bot
client.run(TOKEN)
