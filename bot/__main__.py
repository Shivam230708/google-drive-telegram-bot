import os
import logging
from pyrogram import Client
from bot import (
    APP_ID,
    API_HASH,
    BOT_TOKEN,
    DOWNLOAD_DIRECTORY
)

# Logging Configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(name)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Create download directory if not exists
if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

if name == "main":
    plugins = dict(root="bot/plugins")

    app = Client(
        "G-DriveBot",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=plugins,
        parse_mode="markdown"  # Correct parameter name
    )

    LOGGER.info("Starting Bot...")
    app.run()
    LOGGER.info("Bot Stopped!")
