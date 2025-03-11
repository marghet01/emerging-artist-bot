from datetime import datetime

def format_date(iso_date):
    """Converte la data ISO 8601 in un formato leggibile per l'utente"""
    dt = datetime.fromisoformat(iso_date.replace("Z", ""))
    return dt.strftime("%A %d %B %Y - %H:%M")