from transformers import pipeline

summarizer = pipeline("summarization", model="csebuetnlp/mT5_multilingual_XLSum")

texte = """L’histoire de l’Empire romain est l’une des plus fascinantes de l’Antiquité. Fondée en 27 av. J.-C. 
par Auguste, la Rome impériale a connu une expansion fulgurante, s’étendant de la Bretagne jusqu’au Moyen-Orient. 
Elle a marqué l’histoire par son organisation politique, ses avancées en ingénierie et ses conquêtes militaires. 

Les Romains ont construit des routes, des aqueducs et des amphithéâtres qui existent encore aujourd’hui. 
Le Colisée, par exemple, est un symbole emblématique de leur ingéniosité architecturale. L’armée romaine, 
disciplinée et bien entraînée, a permis à l’Empire de dominer ses adversaires et d’imposer la Pax Romana, 
une période de paix et de prospérité relative qui a duré plus de deux siècles.

Cependant, l’Empire n’a pas été épargné par les crises. La corruption, les invasions barbares et l’instabilité 
politique ont contribué à son déclin. En 476 apr. J.-C., l’Empire romain d’Occident s’effondre avec la destitution 
du dernier empereur, Romulus Augustule. Malgré sa chute, l’héritage romain perdure dans de nombreux aspects 
de notre civilisation moderne, notamment le droit, l’architecture et les langues latines qui ont donné naissance 
au français, à l’espagnol et à l’italien.

Aujourd’hui encore, l’influence de Rome se ressent dans nos sociétés, et son histoire continue de passionner 
historiens et amateurs d’Antiquité."""

resume = summarizer(texte, max_length=100, min_length=30, do_sample=False)

print("🔹 Résumé :", resume[0]["summary_text"])
