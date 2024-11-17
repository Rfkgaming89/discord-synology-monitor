---

# Synology Discord Monitor Bot

A Dockerized Discord bot that monitors disk space and uptime on a Synology NAS. The bot allows you to quickly check the available, used, and total space for `/volume1` and `/volume2` directly from your Discord server.

## Features
- Check disk space for `/volume1` and `/volume2`.
- Display the total combined disk space.
- Monitor NAS system uptime.
- Easy deployment using Docker.

## Prerequisites
- **Synology NAS with DSM 7.0+**
- **Docker (Container Manager)** installed on your Synology NAS.
- A **Discord bot token** from the [Discord Developer Portal](https://discord.com/developers/applications).

## Installation Instructions

### 1. Clone the Repository
Download or clone the repository to your local machine or Synology NAS:

```bash
git clone https://github.com/yourusername/synology-discord-monitor.git
```

### 2. Create a Discord Bot Token
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application.
2. Navigate to **Bot** and create a bot.
3. Copy the generated **bot token**.

### 3. Create the `.env` File
In the root of your project folder (or in `/app` inside Docker), create a `.env` file to store your bot token securely.

#### Example `.env` file:
```
DISCORD_TOKEN=your-discord-bot-token-here
```

Make sure to replace `your-discord-bot-token-here` with the actual bot token from Discord.

### 4. Build and Run the Docker Container
1. **Open Docker** on your Synology NAS.
2. **Download the base image** `python:3.10-slim` from the Docker registry (optional, as the Dockerfile handles this).
3. Open **File Station** and map your local folder containing the bot code to `/app` in the container.
4. Build the Docker container:

```bash
docker build -t synology-discord-monitor /path/to/repo
```

5. Run the container with the `.env` file:

```bash
docker run -d --name discord-bot \
  -v /path/to/local/repo:/app \
  --env-file /path/to/.env \
  synology-discord-monitor
```

This will mount your repository and `.env` file inside the container.

### 5. Verify the Bot
- Check the **Docker logs** to ensure the bot started successfully:
  ```bash
  docker logs discord-bot
  ```
- You should see output like:
  ```
  Logged in as <bot_name>
  Commands synchronized!
  ```

### 6. Invite the Bot to Your Discord Server
1. Go back to the **Discord Developer Portal**, and under **OAuth2 > URL Generator**, select:
   - `bot`
   - `applications.commands`
2. Copy and paste the generated invite URL into your browser and invite the bot to your server.

### 7. Using the Bot
Use the following commands in your Discord server:
- `/uptime` – Displays the NAS uptime.
- `/volume1_space` – Displays disk space for `/volume1`.
- `/volume2_space` – Displays disk space for `/volume2`.
- `/total_space` – Displays total combined space for both volumes.

### 8. Stopping the Bot
To stop the bot, run:
```bash
docker stop discord-bot
```

### 9. Updating the Bot
To update the bot code:
1. Update the code in your local folder.
2. Rebuild the image and restart the container.

```bash
docker build -t synology-discord-monitor /path/to/repo
docker stop discord-bot
docker rm discord-bot
docker run -d --name discord-bot \
  -v /path/to/local/repo:/app \
  --env-file /path/to/.env \
  synology-discord-monitor
```

## Troubleshooting
- **Bot not starting**: Check the Docker logs for errors.
- **Commands not appearing**: Wait a few minutes or restart the container.
- **Disk space issues**: Ensure the paths `/volume1` and `/volume2` are correct for your setup.

## License
This project is licensed under the MIT License.
--
