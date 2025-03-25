import os
import logging
import datetime
import time
import ntplib
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
    return datetime.datetime.now(datetime.UTC)

def sync_time_ntp():
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request("time.google.com", version=3)
        new_time = datetime.datetime.utcfromtimestamp(response.tx_time)
        print(f"✅ Synced UTC Time (from NTP): {new_time}")
    except Exception as e:
        print(f"⚠️ Error in NTP time sync: {e}")

print(f"⏳ System Time Before Sync: {get_system_time()}")
sync_time_ntp()
time.sleep(3)
print(f"⏳ System Time After Sync: {get_system_time()}")

# Load Configurations
API_ID = int(os.getenv("API_ID", Config.API_ID))
API_HASH = os.getenv("API_HASH", Config.API_HASH)
BOT_TOKEN = os.getenv("BOT_TOKEN", Config.BOT_TOKEN)
DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY", Config.DOWNLOAD_DIRECTORY)

if not os.path.isdir(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

# Ensure Pyrogram connects only after time sync
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

LOGGER.info("🚀 Starting Bot...")
app.run()
LOGGER.info("🛑 Bot Stopped!")
