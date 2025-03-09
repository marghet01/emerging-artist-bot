import os
from dotenv import load_dotenv

dotenv_loaded = load_dotenv()
print(f"✅ .env caricato: {dotenv_loaded}")

print(f"📂 Percorso attuale: {os.getcwd()}")

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
print(f"🔑 Token letto: {TOKEN}")

if not TOKEN:
    raise ValueError("❌ ERROR: Token was not found in file .env")