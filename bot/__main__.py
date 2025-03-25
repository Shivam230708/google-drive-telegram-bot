import os
import logging
import datetime
import time
import requests
import subprocess
from pyrogram import Client
from pyrogram.raw.functions import Ping
from bot.config import Config

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

def get_system_time():
    return datetime.datetime.now(datetime.UTC)  # Use timezone-aware UTC

def sync_time():
    try:
        response = requests.get("http://worldtimeapi.org/api/timezone/Etc/UTC")
        if response.status_code == 200:
            current_utc = response.json()["utc_datetime"]
            print(f"✅ Synced UTC Time (from API): {current_utc}")
            
            # ✅ **Try to update system clock (if Railway allows it)**
            try:
                subprocess.run(["date", "-s", current_utc], check=True)
                print(f"✅ System time forcibly set to: {current_utc}")
            except Exception as e:
                print(f"⚠️ Could not set system time: {e}")
        else:
            print("⚠️ Failed to sync time from API")
    except Exception as e:
        print(f"⚠️ Error in time sync: {e}")

print(f"⏳ System Time Before Sync: {get_system_time()}")
sync_time()
time.sleep(5)  # Give time for clock to stabilize
print(f"⏳ System Time After Sync: {get_system_time()}")

# Load Configurations
API_ID = int(os.getenv("API_ID", Config.API_ID))
API_HASH = os.getenv("API_HASH", Config.API_HASH)
BOT_TOKEN = os.getenv("BOT_TOKEN", Config.BOT_TOKEN)
DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY", Config.DOWNLOAD_DIRECTORY)

if not os.path.isdir(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

# ✅ Ensure Pyrogram connects only after successful time sync
with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
    app.send(Ping(ping_id=0))
    print("✅ Telegram time sync successful!")

print(f"📅 Current UTC time: {datetime.datetime.now(datetime.UTC)}")
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
