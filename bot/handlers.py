from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import bot.messages

message = bot.messages

async def start_command(update: Update, context: CallbackContext):
    """Replies to /start command"""
    await update.message.reply_text(message.WELCOME_MESSAGE)

async def help_command(update: Update, context: CallbackContext):
    """Replies to /help command"""
    await update.message.reply_text(message.HELP_MESSAGE)

async def about_command(update: Update, context: CallbackContext):
    """Replies to /about command"""
    await update.message.reply_text(message.ABOUT_MESSAGE)

def get_handlers():
    """Returns command handlers in one list."""
    return [
        CommandHandler("start", start_command),
        CommandHandler("help", help_command),
        CommandHandler("about", about_command),
    ]