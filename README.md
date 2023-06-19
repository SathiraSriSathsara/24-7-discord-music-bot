# Discord 24/7 Music Bot

This is a simple Discord music bot written in Python that can play an MP3 file on a loop in a voice channel.

## Requirements

- Python 3.6 or higher
- FFmpeg
- Discord.py library
- PyNaCl library

## Installation

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/SathiraSriSathsara/24-7-discord-music-bot.git
   ```

2. Install the required dependencies:
   ```shell
   pip3 install discord.py PyNaCl
   ```

3. FFmpeg:
   ```shell
   sudo apt update
   sudo apt install ffmpeg -y
   ```

## Configuration:

- Obtain a Discord bot token by creating a new application in the Discord Developer Portal.
- Open the `bot.py` file and replace the following placeholders with your own values:<br>
         <br> 1. `YOUR_VOICE_CHANNEL_ID`: The ID of the voice channel where you want the bot to join.
         <br> 2. `song.mp3`: The actual path to your MP3 file.
         <br> 3. `YOUR_DISCORD_BOT_TOKEN`: The Discord bot token obtained from the Discord Developer Portal.<br>
         
- Start the bot:
   ```
   python3 bot.py
  ```


## Usage

- Invite the bot to your Discord server using the OAuth2 URL generated in the Discord Developer Portal.
- Type the bot command prefix followed by commands to control the bot. By default, the prefix is set to !.
- The bot will join the specified voice channel and start playing the MP3 file on a loop.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.


<br>

<div align="center">
	<img src="https://github.com/SathiraSriSathsara/SathiraSriSathsara/blob/main/icon.png" width="40">
	<h4>Sathira Sri Sathsara @ 2023</h4>
</div>	

