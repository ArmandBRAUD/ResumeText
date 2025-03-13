import React, { useState } from "react";
import './App.css';

function App() {
  // State pour gérer l'entrée du texte, le résumé et les erreurs
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [minLength, setMinLength] = useState(50); // Longueur minimale du résumé
  const [maxLength, setMaxLength] = useState(100); // Longueur maximale du résumé

  // Fonction pour diviser le texte en morceaux si nécessaire
  const chunkText = (text, chunkSize = 1000) => {
    const words = text.split(" ");
    const chunks = [];
    for (let i = 0; i < words.length; i += chunkSize) {
      chunks.push(words.slice(i, i + chunkSize).join(" "));
    }
    return chunks;
  };

  // Fonction pour envoyer le texte à l'API Flask
  const handleSummarize = async () => {
    if (!text.trim()) {
      alert("Veuillez entrer un texte à résumer !");
      return;
    }

    setLoading(true);

    try {
      // Diviser le texte en morceaux si nécessaire
      const chunkedText = chunkText(text);

      // Envoyer les morceaux de texte à l'API et récupérer les résumés
      const responses = await Promise.all(
        chunkedText.map(async (chunk) => {
          const response = await fetch("http://localhost:5000/summarize", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              text: chunk,
              min_length: minLength,
              max_length: maxLength,
            }),
          });

          return response.json();
        })
      );

      // Combiner les résumés des morceaux
      const fullSummary = responses.map(response => response.summary).join(" ");
      setSummary(fullSummary);

    } catch (error) {
      console.error("Erreur lors de la communication avec l'API:", error);
      setSummary("Erreur de connexion avec l'API.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Résumé de Texte</h1>

      {/* Zone d'entrée pour le texte */}
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows="10"
        cols="50"
        placeholder="Entrez votre texte ici..."
      ></textarea>

      {/* Sélectionner la longueur du résumé */}
      <div>
        <label>
          Longueur minimale du résumé :
          <input
            type="number"
            value={minLength}
            onChange={(e) => setMinLength(parseInt(e.target.value))}
            min="10"
          />
        </label>
      </div>
      <div>
        <label>
          Longueur maximale du résumé :
          <input
            type="number"
            value={maxLength}
            onChange={(e) => setMaxLength(parseInt(e.target.value))}
            max="500"
          />
        </label>
      </div>

      {/* Bouton pour générer le résumé */}
      <div>
        <button onClick={handleSummarize} disabled={loading}>
          {loading ? "En cours..." : "Générer le résumé"}
        </button>
      </div>

      {/* Affichage du résumé */}
      {summary && (
        <div>
          <h3>Résumé :</h3>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
