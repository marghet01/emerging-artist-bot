from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from services.database import get_concerts
from services.functions import format_date
import bot.messages
import re

message = bot.messages

def escape_markdown(text):
    """Escapes special characters for Telegram MarkdownV2"""
    return re.sub(r"([_*\[\]()~`>#\+\-=|{}.!])", r"\\\1", text)


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
    
    reply_city = escape_markdown(city.capitalize())

    if not concerts:
        await update.message.reply_text(f"❌ Nessun concerto trovato a *{reply_city}*", parse_mode="Markdown")
    else:
        response = f"🎶 Concerti a *{reply_city}*:\n\n"

        for c in concerts:
            formatted_date = escape_markdown(format_date(c['date']))
            artist = escape_markdown(c['artist'])
            venue = escape_markdown(c['venue'])
            genre = escape_markdown(c['genre'])
            link = f"[🔗 Link all'evento]({escape_markdown(c['link'])})" if "link" in c and c["link"] else ""
            
            response += (
                f"🎤 *{artist}*\n"
                f"📅 {formatted_date}\n"
                f"📍 {venue}\n"
                f"🎵 {genre}\n"
                f"{link}\n\n"
            )

        await update.message.reply_text(response, parse_mode="MarkdownV2", disable_web_page_preview=True)

def get_handlers():
    """Returns command handlers in one list."""
    return [
        CommandHandler("start", start_command),
        CommandHandler("help", help_command),
        CommandHandler("about", about_command),
        CommandHandler("concert", concert_command)
    ]