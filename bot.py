import psutil
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load the environment variables from .env file
load_dotenv()

# Get the bot token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a bot instance with intents and a command prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Command to check uptime of the bot
@bot.tree.command()
async def uptime(interaction: discord.Interaction):
    try:
        # Get system uptime
        uptime_seconds = psutil.boot_time()
        current_time = psutil.time.time()
        uptime = current_time - uptime_seconds
        uptime_days = uptime // (24 * 3600)
        await interaction.response.send_message(f"Bot uptime: {int(uptime_days)} days")
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")
        print(f"Error in command 'uptime': {e}")

# Command to check total disk space of both volumes in TB
@bot.tree.command()
async def total_space(interaction: discord.Interaction):
    try:
        # Get usage for /volume1
        usage_volume1 = psutil.disk_usage('/volume1')
        total_volume1_tb = usage_volume1.total / (1024 ** 4)  # Convert to TB

        # Get usage for /volume2
        usage_volume2 = psutil.disk_usage('/volume2')
        total_volume2_tb = usage_volume2.total / (1024 ** 4)  # Convert to TB

        # Combine the total space of both volumes
        combined_total_tb = total_volume1_tb + total_volume2_tb
        
        await interaction.response.send_message(f"**Combined Total Space:**\nTotal: {combined_total_tb:.2f} TB")
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")
        print(f"Error in command 'total_space': {e}")

# Command to check disk space for /volume1 in TB
@bot.tree.command()
async def volume1_space(interaction: discord.Interaction):
    try:
        usage = psutil.disk_usage('/volume1')
        total_tb = usage.total / (1024 ** 4)  # Convert to TB
        used_tb = usage.used / (1024 ** 4)  # Convert to TB
        free_tb = usage.free / (1024 ** 4)  # Convert to TB

        await interaction.response.send_message(
            f"**/volume1:**\nTotal: {total_tb:.2f} TB\nUsed: {used_tb:.2f} TB\nFree: {free_tb:.2f} TB"
        )
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")
        print(f"Error in command 'volume1_space': {e}")

# Command to check disk space for /volume2 in TB
@bot.tree.command()
async def volume2_space(interaction: discord.Interaction):
    try:
        usage = psutil.disk_usage('/volume2')
        total_tb = usage.total / (1024 ** 4)  # Convert to TB
        used_tb = usage.used / (1024 ** 4)  # Convert to TB
        free_tb = usage.free / (1024 ** 4)  # Convert to TB

        await interaction.response.send_message(
            f"**/volume2:**\nTotal: {total_tb:.2f} TB\nUsed: {used_tb:.2f} TB\nFree: {free_tb:.2f} TB"
        )
    except Exception as e:
        await interaction.response.send_message(f"Error: {e}")
        print(f"Error in command 'volume2_space': {e}")

# Start the bot and sync the commands
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        await bot.tree.sync()  # Force sync the slash commands
        print("Commands synchronized!")
    except Exception as e:
        print(f"Error synchronizing commands: {e}")

# Run the bot
bot.run(TOKEN)
