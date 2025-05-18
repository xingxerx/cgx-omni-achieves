import discord
import os

# Get your Discord bot token from environment variables
# It's important to keep your token secret!
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

class CGXDiscordBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        # Don't respond to ourselves
        if message.author == self.user:
            return

        # Example: Respond to a command
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

# Create and run the bot
intents = discord.Intents.default()
intents.message_content = True # You need this intent to read message content
bot = CGXDiscordBot(intents=intents)
bot.run(DISCORD_TOKEN)
