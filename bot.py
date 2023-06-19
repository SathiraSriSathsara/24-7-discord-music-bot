import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready.')

    # Join the voice channel and start playing the MP3 file on loop
    channel_id = YOUR_VOICE_CHANNEL_ID  # Replace with your voice channel ID
    file_path = 'song.mp3'  # Replace with the actual path to your MP3 file

    channel = bot.get_channel(channel_id)
    if not channel:
        return print('Invalid voice channel ID.')

    voice_client = await channel.connect()
    
    while True:
        voice_client.play(discord.FFmpegPCMAudio(file_path))
        await asyncio.sleep(voice_client.source.duration)
        voice_client.stop()

bot.run('YOUR_DISCORD_BOT_TOKEN')  # Replace with your Discord bot token
