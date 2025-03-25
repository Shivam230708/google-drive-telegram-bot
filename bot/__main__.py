import time
import datetime
import os

# System clock ko sync karne ki koshish
os.system("date")

# Telegram server se exact time sync karna
from pyrogram import Client
from pyrogram.raw.functions import Ping

with Client("my_account") as app:
    app.send(Ping(ping_id=0))
    print("Telegram time sync successful!")

print(f"Current UTC time: {datetime.datetime.utcnow()}")
time.sleep(2)  # Small delay before Pyrogram starts

import os
import logging
from pyrogram import Client
from bot import (
  APP_ID,
  API_HASH,
  BOT_TOKEN,
  DOWNLOAD_DIRECTORY
  )

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__":
    if not os.path.isdir(DOWNLOAD_DIRECTORY):
        os.makedirs(DOWNLOAD_DIRECTORY)
    plugins = dict(
        root="bot/plugins"
    )
    app = Client(
        "G-DriveBot",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins,
        parse_mode="markdown",
        workdir=DOWNLOAD_DIRECTORY
    )
    LOGGER.info('Starting Bot !')
    app.run()
    LOGGER.info('Bot Stopped !')
