import React, { useState } from 'react';

function Summarizer() {
  const [text, setText] = useState('');
  const [summary, setSummary] = useState('');

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const generateSummary = async () => {
    try {
      const response = await fetch('http://localhost:5000/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });

      const data = await response.json();
      setSummary(data.summary);
    } catch (error) {
      console.error('Erreur lors de la génération du résumé', error);
    }
  };

  return (
    <div>
      <textarea
        placeholder="Entrez votre texte ici..."
        value={text}
        onChange={handleTextChange}
        rows="10"
        cols="50"
      ></textarea>
      <br />
      <button onClick={generateSummary}>Générer le résumé</button>
      <h3>Résumé :</h3>
      <p>{summary}</p>
    </div>
  );
}

export default Summarizer;
