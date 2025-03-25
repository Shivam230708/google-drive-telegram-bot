import os
import logging
import datetime
import time
from pyrogram import Client

# Logging setup
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

# Load Configurations
API_ID = int(os.getenv("API_ID", "26079994"))  # Replace with actual API_ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with actual API_HASH
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")  # Replace with actual BOT_TOKEN

# ✅ Using Telegram server time instead of NTP
def get_telegram_time():
    with Client("temp_sync", api_id=API_ID, api_hash=API_HASH) as app:
        return app.get_me().date

telegram_time = get_telegram_time()
print(f"✅ Synced UTC Time from Telegram: {telegram_time}")

# Ensure Pyrogram connects only after time sync
with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
    app.send_message("me", f"✅ Bot started at Telegram Time: {telegram_time}")
    print("✅ Telegram time sync successful!")

print(f"📅 Current UTC time: {datetime.datetime.utcnow()}")
time.sleep(2)

# Initialize Pyrogram Bot
app = Client(
    "G-DriveBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

LOGGER.info("🚀 Starting Bot...")
app.run()
LOGGER.info("🛑 Bot Stopped!")
