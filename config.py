import os
from dotenv import load_dotenv
import telebot

load_dotenv()

ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN NOT FOUND")
bot = telebot.TeleBot(TOKEN)

DB_NAME = "ballestero_sayings.db"

DB_CURRENT_VERSION = 1
