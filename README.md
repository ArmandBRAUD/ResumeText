# ResumeText

**ResumeText** est un projet Python conçu pour réaliser des résumés automatiques de textes à l'aide de modèles de traitement du langage naturel. Il utilise des techniques de résumé extractif et abstrait pour condenser des textes tout en préservant leurs informations essentielles.

## Installation

### Prérequis

Assurez-vous que Python 3.x est installé sur votre machine. Vous pouvez vérifier cela avec :

```bash
python --version
Configuration de l'environnement virtuel
Il est recommandé de créer un environnement virtuel afin d'isoler les dépendances du projet. Pour ce faire :


# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sous Windows :
.\venv\Scripts\activate
# Sous Mac/Linux :
source venv/bin/activate
Installation des dépendances
Avec l'environnement virtuel activé, installez les dépendances nécessaires en exécutant :


pip install -r requirements.txt
Cela installera toutes les bibliothèques requises (comme spaCy, transformers, sumy, etc.) pour le traitement du langage naturel.

Utilisation
Exécution du script de résumé
Le fichier test_summarizer.py propose un exemple de script qui utilise deux approches de résumé : Sumy (LSA) et mT5 (Transformers).

Pour exécuter le script :


python test_summarizer.py
Le script génère un résumé basé sur les modèles configurés. Vous pouvez remplacer le texte par défaut en modifiant la variable texte dans ce fichier.

Personnalisation du texte à résumer
Pour adapter le texte à résumer, éditez la variable texte dans test_summarizer.py :

python
Copier
Modifier
texte = """Votre texte personnalisé ici"""
Après modification, relancez le script pour obtenir le résumé adapté.

Paramétrage du modèle mT5
Le modèle mT5 vous permet de définir la longueur du résumé grâce aux paramètres max_length et min_length. Par exemple, pour un résumé compris entre 50 et 100 mots :

python
Copier
Modifier
resume = summarizer(texte, max_length=100, min_length=50, do_sample=False)
Utilisation de Sumy (LSA)
Si vous préférez l'approche basée sur Sumy (LSA) pour un résumé sémantique, utilisez la fonction resumer_sumy() :

python
Copier
Modifier
print(resumer_sumy(texte, nb_phrases=2))
Ceci génère un résumé composé de 2 phrases principales, sélectionnées via l'analyse sémantique.

Exemple de texte à résumer
Voici un exemple de texte pour tester le projet :

plaintext
Copier
Modifier
L'intelligence artificielle est un domaine en pleine expansion qui révolutionne de nombreux secteurs comme la santé, 
les finances et les transports. Grâce aux algorithmes de machine learning, les entreprises peuvent automatiser des tâches, 
analyser des données massives et améliorer leurs prises de décisions. Toutefois, cette avancée technologique soulève aussi 
des questions éthiques et des défis liés à la confidentialité et à la sécurité des informations personnelles.
Contribuer
Pour contribuer à ce projet :

Forkez ce projet.
Créez une branche pour votre fonctionnalité :

git checkout -b feature/ma-fonctionnalite
Effectuez vos modifications et committez-les :

git commit -am 'Ajout de fonctionnalité'
Poussez votre branche :

git push origin feature/ma-fonctionnalite
Créez une pull request.
Auteurs Armand BRAUD - Créateur et développeur principal

Ce fichier est entièrement contenu dans un seul document et présente une structure uniforme et claire.