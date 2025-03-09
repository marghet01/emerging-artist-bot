import json, os

CONCERTS_FILE = 'concerts_test.json'

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


def get_concerts(city):
    """Returns concerts based on the city"""
    concerts = load_concert()
    return filter_by_city(concerts, city)