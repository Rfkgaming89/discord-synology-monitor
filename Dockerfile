# Use official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the bot.py and .env files into the container
COPY bot.py /app/
COPY .env /app/

# Install required Python packages
RUN pip install --no-cache-dir discord.py python-dotenv psutil

# Command to run the bot
CMD ["python", "bot.py"]
