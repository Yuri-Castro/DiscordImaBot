
import discord
from discord.ext import commands

from gtts import gTTS
from dotenv import load_dotenv

import aiofiles as aiof
import os
import random

import utils
import asyncio

import numpy as np

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)

    @commands.Cog.listener()
    async def on_message(self, message):
        print('eae wernao')
        print(message)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after ):

        # User join
        if before.channel == None and after.channel != None:
            await asyncio.sleep(2)
            user = member.name
            if user != 'ImaBot':
                    
                # await member.guild.system_channel.send(f'Hello {user}')

                channel = after.channel.name
                
                speech_text = 'Ó LÁ, Os amigos brigando' if user == 'mrcastro2' else f'Hello {user}'



                await utils.text_to_speech(speech_text, after, member)

        # else:
    # #     await ctx.send('User is not in a channel.')
    #     import ipdb; ipdb.set_trace()
    #     x = 2
@bot.command(
    name='game',
    description='Select a random game for imaplaying',
    pass_context=True,
)
async def game(ctx):
    # grab the user who sent the command
    # speech_text = ' '.join(ctx.message.content.split(' ')[1:])
    speech_text = 'Isso é ' + random.choice([ 'Amonga', 'racs', 'gartic', 'stop']) + ' Porra!'
    user=ctx.message.author
    
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # grab user's voice channel
        channel=voice_channel.name
        await ctx.send('User is in channel: '+ channel)
        # create StreamPlayer
        
        if user.guild.voice_client == None:
            vc= await voice_channel.connect()
        else:
            vc = user.guild.voice_client 
        speech_file = await utils.generate_audio_text_file(text=speech_text)

        vc.play(discord.FFmpegPCMAudio(speech_file), after=lambda e: print('done', e))

        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
        await vc.disconnect()
    # else:
        # await ctx.send('User is not in a channel.')


@bot.command(
    name='coach',
    description='Select your size',
    pass_context=True,
)
async def size(ctx):

    text = 'Valeu coachzão!'

    await ctx.send(text)



bot.add_cog(Events(bot))
bot.run(TOKEN)