API de Résumé de Texte avec Flask et React

Ce projet permet de générer un résumé automatique de texte en utilisant Flask pour l'API backend et React pour le frontend. Il utilise le modèle mT5_multilingual_XLSum de Hugging Face pour effectuer le résumé.

📌 Prérequis

Avant de commencer, assure-toi d'avoir installé :

Python 3.x

Node.js (avec npm ou yarn)

pip pour installer les dépendances Python

git (optionnel, mais recommandé)

⚙️ Installation du Backend (API Flask)

Cloner le projet :

    git clone https://github.com/ton-repo/text-summarizer.git
    cd text-summarizer
Créer un environnement virtuel (optionnel mais recommandé) :
    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    
Installer les dépendances du backend :
    pip install -r requirements.txt
    
Lancer l'API Flask :
    python app.py
L'API tourne maintenant sur : http://localhost:5000/summarize

🌍 Installation et Lancement du Frontend (React)

Accéder au dossier du frontend :
    cd frontend
    
Installer les dépendances :
    npm install  # ou yarn install
    
Lancer le serveur React :
    npm start  # ou yarn start

Accéder à l'application web :
📍 http://localhost:3000/

🔥 Comment Utiliser ?

Entrer un texte dans l'interface web.
Définir la longueur minimale et maximale du résumé (optionnel).
Cliquer sur "Générer le résumé".

🛠 Problèmes Courants et Solutions

❌ Problème de Modèle

Si le modèle de Hugging Face ne se charge pas correctement, essaie de le retélécharger :

pip uninstall transformers
pip install transformers

❌ API Inaccessible depuis React

Vérifie que l'API tourne bien sur localhost:5000 et que l'URL utilisée dans le frontend correspond à celle de l'API.

🐝 Fichiers Importants

app.py → API Flask

requirements.txt → Dépendances Python

frontend/ → Code source React
