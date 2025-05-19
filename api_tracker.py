import json
import time
import os
from datetime import datetime, timedelta

# === CONFIGURATION ===
LOG_FILE = "api_log.json"
LIMIT = 150
WINDOW_SECONDS = 15 * 60  # 15 minutes

# === UTILS ===
def now_ts():
    return time.time()

def load_log():
    if not os.path.exists(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_log(timestamps):
    with open(LOG_FILE, "w") as f:
        json.dump(timestamps, f)

def cleanup_old(timestamps):
    return [ts for ts in timestamps if ts > now_ts() - WINDOW_SECONDS]

# === MAIN FUNCTION ===
def count_request():
    timestamps = load_log()
    timestamps = cleanup_old(timestamps)

    if len(timestamps) >= LIMIT:
        # Trop de requêtes : calcul du temps d'attente
        oldest = min(timestamps)
        retry_time = datetime.fromtimestamp(oldest + WINDOW_SECONDS)
        wait_seconds = int((oldest + WINDOW_SECONDS) - now_ts())

        minutes = wait_seconds // 60
        seconds = wait_seconds % 60

        print(f"⛔️ Tu as dépassé {LIMIT} requêtes en 15 minutes.")
        print(f"🕒 Réessaie dans {minutes} min {seconds} sec (à {retry_time.strftime('%H:%M:%S')})")
        exit(1)

    # Ajoute l'appel
    timestamps.append(now_ts())
    save_log(timestamps)

    print(f"📡 Requête API #{len(timestamps)}/{LIMIT} (dans les 15 dernières minutes)")
