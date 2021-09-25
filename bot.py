# Discord imports
import discord
from discord.ext import commands

from config import (
    bot_config,
    TOKEN_KEY,
    COMMANDS_PREFIX_KEY,
    BOT_DESCRIPTION_KEY
    # FILL: Insert other configuration keys needed here... 
)

# Bot
bot = commands.Bot(
    command_prefix=bot_config[COMMANDS_PREFIX_KEY], 
    intents=discord.Intents.all(), 
    description=bot_config[BOT_DESCRIPTION_KEY]
)

# Cogs
""" 
    FILL: Add instances of Cogs here. 

    Example: 
    music_cog = Music(bot)
"""

# Events and Commands 

@bot.event
async def on_ready():
    """
    Event triggered when bot is ready for commands
    """
    print("Logged in as {0.user}".format(bot))

@bot.command()
async def ping(ctx):
    """
    Ping-pong bot presence confirmation command
    """
    await ctx.send("pong")

# Add cogs
"""
    Add Cogs to bot.

    Example:
    bot.add_cog(music_cog)
"""

# Start bot
bot.run(bot_config[TOKEN_KEY])