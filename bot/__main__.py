import os
import logging
import datetime
import time
import pytz  # Add this for timezone
from pyrogram import Client
from pyrogram.raw.functions import Ping
from bot.config import Config  # Ensure config.py is properly structured

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# Fetching Environment Variables
API_ID = int(os.getenv("API_ID", Config.API_ID))  # Ensure API_ID is an integer
API_HASH = os.getenv("API_HASH", Config.API_HASH)
BOT_TOKEN = os.getenv("BOT_TOKEN", Config.BOT_TOKEN)
DOWNLOAD_DIRECTORY = os.getenv("DOWNLOAD_DIRECTORY", Config.DOWNLOAD_DIRECTORY)

# Ensure directory exists
if not os.path.isdir(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)

# **Force Time Sync**
try:
    os.system("sudo ntpdate -s time.nist.gov")
except Exception as e:
    print("NTP Time Sync Failed, proceeding anyway...")

# **Check and print system time**
utc_time = datetime.datetime.now(pytz.utc)
print(f"System UTC Time: {utc_time}")

# Telegram Server Time Sync
with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
    app.send(Ping(ping_id=0))
    print("Telegram time sync successful!")

print(f"Current UTC time after sync: {datetime.datetime.utcnow()}")
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
