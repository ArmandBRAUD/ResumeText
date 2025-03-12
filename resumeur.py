import spacy
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from transformers import pipeline

# Charger spaCy pour le prétraitement
nlp = spacy.load("en_core_web_sm")
nltk.download('punkt')

# Modèle de résumé en français
summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")

# Texte d'exemple
texte = """
L’intelligence artificielle est un domaine en pleine expansion qui révolutionne de nombreux secteurs comme la santé, 
les finances et les transports. Grâce aux algorithmes de machine learning, les entreprises peuvent automatiser des tâches, 
analyser des données massives et améliorer leurs prises de décisions. Toutefois, cette avancée technologique soulève aussi 
des questions éthiques et des défis liés à la confidentialité et à la sécurité des informations personnelles.
"""

# 🔹 Option 1 : Résumé avec Sumy (LSA)
def resumer_sumy(text, nb_phrases=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))  # ⚠️ Tester avec "french" si ça fonctionne
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, nb_phrases)
    return " ".join(str(sentence) for sentence in summary)

# 🔹 Option 2 : Résumé avec un modèle pré-entraîné (mT5)
def resumer_transformers(text):
    return summarizer(text, max_length=100, min_length=50, do_sample=False)[0]["summary_text"]

# Affichage des résumés
print("📌 Résumé avec Sumy :")
print(resumer_sumy(texte))

print("\n📌 Résumé avec mT5 :")
print(resumer_transformers(texte))
