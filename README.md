# 🎮 Trophy Tracker

Application en Python permettant de suivre ses trophées PSN, organiser ses jeux en cours, visualiser les trophées platine, et associer des guides.

Technologies utilisées : Python, API PSN, SQLite, Tkinter, Matplotlib

Bien sûr Franck ! Voici un tableau clair et prêt à être copié dans ton `README.md` pour documenter les méthodes disponibles via `psnawp-api`. Il est formaté en **Markdown**, donc tu peux le coller directement dans ton fichier sans rien adapter.

---

## ✅ Version alternative — lisible, propre, mobile-friendly :


---

### 🎮 Méthodes principales — Utilisateur et jeux

* **`psn.user(online_id="pseudo")`**
  → Récupère un utilisateur PSN à partir de son pseudo.
  *Exemple :* `user = psn.user(online_id="francky_rototo")`

* **`user.account_id`**
  → Identifiant unique de l’utilisateur (fixe, non modifiable).
  *Exemple :* `account_id = user.account_id`

* **`user.trophy_titles()`**
  → Liste tous les jeux avec trophées de l’utilisateur.
  *Exemple :* `titles = user.trophy_titles()`

* **`title.title_name`**
  → Nom du jeu.
  *Exemple :* `title.title_name`

* **`title.title_platform`**
  → Plateforme (PS4, PS5…).
  *Exemple :* `title.title_platform`

* **`title.progress`**
  → Pourcentage de progression des trophées.
  *Exemple :* `title.progress`

* **`title.np_communication_id`**
  → ID unique du jeu (utile pour les trophées).
  *Exemple :* `title.np_communication_id`

* **`title.defined_trophies`**
  → Nombre total de trophées (bronze, argent, or, platine).
  *Exemple :* `title.defined_trophies`

* **`title.earned_trophies`**
  → Nombre de trophées obtenus par type.
  *Exemple :* `title.earned_trophies`

---

### 🏆 Méthodes trophées — Pour un jeu

* **`user.trophies("np_communication_id")`**
  → Liste tous les trophées d’un jeu.
  *Exemple :* `trophies = user.trophies("NPWR12345_00")`

* **`trophy.trophy_name`**
  → Nom du trophée.
  *Exemple :* `trophy.trophy_name`

* **`trophy.trophy_type`**
  → Type de trophée (bronze, argent, or, platine).
  *Exemple :* `trophy.trophy_type`

* **`trophy.trophy_earned_rate`**
  → Taux mondial d’obtention.
  *Exemple :* `trophy.trophy_earned_rate`

* **`trophy.earned`**
  → Trophée obtenu ou non (booléen).
  *Exemple :* `trophy.earned`

* **`trophy.earned_date_time`**
  → Date d’obtention du trophée (si débloqué).
  *Exemple :* `trophy.earned_date_time`

---

### 🔍 Méthodes complémentaires

* **`psn.search_users("pseudo")`**
  → Recherche un joueur PSN.
  *Exemple :* `results = psn.search_users("TonPseudo")`

* **`psn.search_games("titre")`**
  → Recherche de jeux PSN par nom.
  *Exemple :* `results = psn.search_games("Bloodborne")`

* **`psn.get_game_title("np_communication_id")`**
  → Infos sur un jeu spécifique.
  *Exemple :* `game = psn.get_game_title("NPWR00001_00")`

---
