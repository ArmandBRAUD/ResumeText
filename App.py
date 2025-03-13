from flask import Flask, request, jsonify
from flask_cors import CORS  # Importer CORS
from transformers import pipeline
import re

def clean_summary(text):
    # Liste de mots-clés indésirables
    unwanted_phrases = ["BBC", "journalistes africains", "Kunio Romano"]
    for phrase in unwanted_phrases:
        text = re.sub(phrase, "", text, flags=re.IGNORECASE)
    return text.strip()

app = Flask(__name__)
CORS(app)

# Utilisation d'un modèle plus précis pour éviter les hallucinations
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_chunk_length=1000):
    words = text.split()
    chunks = [" ".join(words[i:i+max_chunk_length]) for i in range(0, len(words), max_chunk_length)]
    return chunks

@app.route('/summarize', methods=['POST'])
def summarize_text():
    try:
        data = request.get_json()
        text = data.get('text')
        min_length = data.get('min_length', 50)
        max_length = data.get('max_length', 100)

        if not text:
            return jsonify({"error": "Le texte est requis"}), 400
        if not isinstance(min_length, int) or not isinstance(max_length, int) or min_length > max_length:
            return jsonify({"error": "min_length et max_length doivent être valides"}), 400

        chunks = chunk_text(text)
        summaries = []

        for chunk in chunks:
            raw_summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]
            cleaned_summary = clean_summary(raw_summary)
            summaries.append(cleaned_summary)

        full_summary = " ".join(summaries)
        return jsonify({"summary": full_summary})

    except Exception as e:
        return jsonify({"error": f"Erreur : {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)