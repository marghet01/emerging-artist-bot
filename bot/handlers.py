from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from services.database import get_concerts
import bot.messages
from services.functions import format_date

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


async def concert_command(update: Update, context: CallbackContext):
    """Replies with a list of concerts in the selected city"""
    if not context.args:
        await update.message.reply_text("❌ Devi specificare una città! Esempio: /concerti Milano")
        return
    
    city = " ".join(context.args)
    concerts = get_concerts(city)
    
    reply_city = city.capitalize()

    if not concerts:
        await update.message.reply_text(f"❌ Nessun concerto trovato a {reply_city}")
    else:
        response = f"🎶 Concerti a {reply_city}:\n"
        for c in concerts:
            formatted_date = format_date(c['date'])
            response += f"- {c['artist']} 📅 {formatted_date} @ {c['venue']}\n"
        await update.message.reply_text(response)

def get_handlers():
    """Returns command handlers in one list."""
    return [
        CommandHandler("start", start_command),
        CommandHandler("help", help_command),
        CommandHandler("about", about_command),
        CommandHandler("concert", concert_command)
    ]