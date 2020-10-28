import uuid
import asyncio
from gtts import gTTS
import discord
import os
async def text_to_speech(speech_text: str, voice_channel : discord.VoiceChannel, member : discord.Member):
                
    # create StreamPlayer
    
    vc = None
    if member.guild.voice_client == None:
        vc= await voice_channel.channel.connect()
    else:
        vc = member.guild.voice_client
    
    speech_file = await generate_audio_text_file(text=speech_text)

    while vc.is_playing():
        await asyncio.sleep(1)
        
    vc.play(discord.FFmpegPCMAudio(speech_file), after=lambda e: print('done', e))

    while vc.is_playing():
        await asyncio.sleep(1)
    
    # disconnect after the player has finished
    # vc.stop()
    # await vc.disconnect()

    os.remove(speech_file)

async def generate_audio_text_file(text: str):
    speech = gTTS(text=text, lang='pt', slow=False) 
    _id = uuid.uuid4().hex
    
    filename = f"./speechs/{_id}_speech.mp3"
    speech.save(filename)
    return filename



