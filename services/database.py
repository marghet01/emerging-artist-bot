import json, os
from datetime import datetime, timedelta

CONCERTS_FILE = 'data/concerts.json'

if not os.path.exists(CONCERTS_FILE):
    print(f"❌ Il file {CONCERTS_FILE} non esiste!")


def load_concert():
    """Load concerts from JSON file"""
    try:
        with open(CONCERTS_FILE, 'r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ File non trovato!")
        return []
    except json.JSONDecodeError:
        print("❌ Errore nella decodifica del JSON!")
        return []


def filter_by_city(concerts, city):
    """Filters concerts by city"""
    city_lower = city.lower()
    return [c for c in concerts if c["city"].lower() == city_lower]


def filter_by_week(concerts):
    """Filters concerts happening in the next 7 days"""
    today = datetime.now()
    week_later = today + timedelta(days=7)

    return [
        c for c in concerts 
        if today <= datetime.fromisoformat(c["date"].replace("Z", "")) <= week_later
    ]


def get_concerts(city):
    """Returns concerts based on the city"""
    concerts = load_concert()
    concerts_by_city = filter_by_city(concerts, city)
    return filter_by_week(concerts)