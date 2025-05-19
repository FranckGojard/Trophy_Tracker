from psn_api import obtenir_account_id, lister_games
from api_tracker import count_request


pseudo = "francky_rototo"
account_id = obtenir_account_id(pseudo)

jeux = lister_games(account_id)

# for jeu in jeux:
#     plateformes = ", ".join(jeu['plateforme'])
#     print(f"{jeu['nom']} ({plateformes}) - {jeu['pourcentage']}% {jeu['np_communication_id']}")


