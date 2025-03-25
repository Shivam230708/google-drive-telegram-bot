import os
import logging
import datetime
import time
import requests
from pyrogram import Client
from pyrogram.raw.functions import Ping
from bot.config import Config as config

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

# Fetching Environment Variables
API_ID = int(os.getenv("API_ID", config.API_ID))
API_HASH = os.getenv("API_HASH", config.API_HASH)
BOT_TOKEN = os.getenv("BOT_TOKEN", config.BOT_TOKEN)
DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY", config.DOWNLOAD_DIRECTORY)

# Ensure directory exists
if not os.path.isdir(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

# ✅ Fix Time Sync Before Telegram Connect
def sync_time():
    try:
        # Attempt to use system time sync
        if os.system("which ntpdate") == 0:
            os.system("sudo ntpdate -u pool.ntp.org")
            print("✅ System time synced using ntpdate.")
        else:
            # Fallback to API time sync
            response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
            if response.status_code == 200:
                current_utc = response.json()["utc_datetime"]
                print(f"✅ Synced UTC Time: {current_utc}")
            else:
                print("⚠️ Failed to sync time from API")
    except Exception as e:
        print(f"⚠️ Error in time sync: {e}")

sync_time()

# Telegram Server Time Sync
with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
    try:
        app.send(Ping(ping_id=0))
        print("✅ Telegram time sync successful!")
    except Exception as e:
        print(f"⚠️ Telegram time sync failed: {e}")

print(f"📅 Current UTC time: {datetime.datetime.utcnow()}")
time.sleep(2)

# Initialize Pyrogram Bot
plugins = dict(root="bot/plugins")

app = Client(
    "G-DriveBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=plugins,
    parse_mode="markdown",
    workdir=DOWNLOAD_DIRECTORY
)

LOGGER.info("Starting Bot...")
app.run()
LOGGER.info("Bot Stopped!")
