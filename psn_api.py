"""
psn_api.py — Gère la connexion à l’API PSN et l’identification de l’utilisateur.
"""

import json
from psnawp_api import PSNAWP
from psnawp_api.models.trophies import PlatformType

def charger_token():
    """
    Lit le fichier config.json et retourne l'access_token.
    """
    with open("config.json", "r") as f:
        config = json.load(f)
    return config["access_token"]

def initialiser_connexion():
    """
    Initialise la connexion API avec le token.
    """
    token = charger_token()
    return PSNAWP(token)

def obtenir_account_id(pseudo: str) -> str:
    """
    Récupère l'account_id PSN à partir du pseudo.

    Args:
        pseudo (str): Pseudo PSN public

    Returns:
        str: account_id unique de l'utilisateur
    """
    psn = initialiser_connexion()
    utilisateur = psn.user(online_id=pseudo)
    return utilisateur.account_id

def lister_games(account_id: str) -> list:
    psn = initialiser_connexion()
    user = psn.user(account_id=account_id)
    
    games = user.trophy_titles()

    my_games = []
    for game in games:
        my_games.append({
            "nom": game.title_name,
            "plateforme": [p.value for p in game.title_platform],
            "pourcentage": game.progress,
            "np_communication_id": game.np_communication_id,
            "defined": game.defined_trophies,
            "earned": game.earned_trophies
        })

    for trophy in user.trophies("NPWR39144_00", PlatformType.PS5):
        print(trophy)

    return my_games
