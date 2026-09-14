# 🐍 Snake Game — Pygame POO

Un jeu **Snake** moderne et interactif développé en **Python avec Pygame**. Ce projet a été réalisé dans le cadre de mon apprentissage de la **Programmation Orientée Objet (POO)**, ce qui m'a permis de structurer le code de manière propre, modulaire et évolutive.

---

## 🎮 Fonctionnalités

* **Menu principal interactif** : Une interface d'accueil soignée.
* **Gestion des difficultés** : 3 modes de jeu (Facile, Normal, Difficile) qui ajustent la vitesse.
* **Double configuration de contrôle** : Jouable au clavier ou à la souris dans les menus.
* **Système de score** : Suivi du score actuel et persistance du **meilleur score** (sauvegardé localement).
* **Physique du jeu** : Détection précise des collisions (murs et corps du serpent).
* **Écran Game Over animé** : Une transition fluide à la fin de la partie.
* **Direction artistique** : Interface graphique au style pixel art rétro.

---

## 🕹️ Contrôles

| Écran | Action | Contrôles |
| :--- | :--- | :--- |
| **Menu Principal** | Naviguer & Valider | `Entrée` / `Espace` / Clic Souris |
| **Sélection Difficulté** | Choisir le mode | `↑` `↓` pour naviguer, `Entrée` pour valider / Souris |
| **En Jeu** | Diriger le serpent | `↑` `↓` `←` `→` (Flèches directionnelles) |
| **Game Over** | Recommencer ou Quitter | `R` pour Rejouer · `M` pour retourner au Menu |

---

## 📁 Structure du Projet

L'architecture du code suit les principes de la POO, séparant distinctement les responsabilités de chaque entité :

```text
snake/
├── assets/             # Images, polices de caractères et ressources graphiques
├── food.py             # Classe de gestion de la nourriture (position, réapparition)
├── game.py             # Classe principale (boucle de jeu, états, menus, collisions)
├── main.py             # Point d'entrée de l'application
├── setting.py          # Constantes du jeu (couleurs, dimensions, vitesses)
├── snake.py            # Classe de gestion du serpent (mouvements, grandissement)
├── .gitignore          # Fichiers à ignorer par Git (ex: .venv, __pycache__)
├── README.md           # Documentation du projet
└── requirements.txt    # Dépendances du projet
```

---

## ⚙️ Installation & Lancement

Suivez ces étapes pour installer et lancer le jeu sur votre machine locale :

### 1. Cloner le dépôt
```bash
git clone https://github.com/Erico06-lls/Snake-Game
cd snake
```

### 2. Configurer l'environnement virtuel
```bash
# Création de l'environnement virtuel
python3 -m venv .venv

# Activation (Linux / macOS)
source .venv/bin/activate

# Activation (Windows - PowerShell)
# .venv\Scripts\Activate.ps1
```

### 3. Installer les dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Démarrer le jeu
```bash
python3 main.py
```

---

## 🛠️ Technologies utilisées

* **Python 3** : Langage de programmation principal.
* **Pygame** : Bibliothèque pour le rendu graphique, la gestion des fenêtres et des entrées utilisateur.
* **POO (Programmation Orientée Objet)** : Encapsulation des données et modularité du code.

---

## 🚀 Évolutions futures (Roadmap)

* [ ] **Audio** : Ajout d'effets sonores (quand le serpent mange) et d'une musique de fond rétro.
* [ ] **Gameplay** : Intégration d'un système de pause en plein jeu (`Échap` ou `P`).
* [ ] **Bonus** : Ajout de plusieurs types de nourriture (fruits rares qui donnent plus de points ou des bonus de vitesse).
* [ ] **Persistence** : Création d'un tableau des scores (Top 5) persistant dans un fichier JSON.
* [ ] **Distribution** : Compilation du projet sous forme d'un exécutable (`.exe` ou `.app`) avec PyInstaller.
