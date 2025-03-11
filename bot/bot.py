from telegram.ext import Application
from config.config import TOKEN
from bot.handlers import get_handlers

def main():
    """Starts Telegram Bot"""
    application = Application.builder().token(TOKEN).build()

    # Adding bot's commands
    for handler in get_handlers():
        application.add_handler(handler)

    print("✅ Bot started!")
    application.run_polling()