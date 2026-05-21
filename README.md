# Devoir - Sensibilisation au phishing

Ce mini-projet contient une maquette locale et fictive pour un devoir de sensibilisation au phishing en milieu scolaire.

## Fichiers

- `index.html` : page principale avec la maquette du faux e-mail, le scénario et l'analyse.
- `styles.css` : mise en page et identité visuelle.
- `login-simulation.html` : page de connexion fictive et locale pour illustrer la suite d'un lien de phishing.
- `login-simulation.css` : mise en page de la page de connexion fictive.
- `server.py` : serveur local qui enregistre les identifiants fictifs dans `captures.json`.

## Utilisation

1. Démarrer le serveur local : `python server.py`
2. Ouvrir `http://localhost:8765/login-simulation.html`
3. Tester le parcours : e-mail -> Suivant -> mot de passe -> Suivant
4. Les identifiants fictifs sont enregistrés dans `captures.json` sur ta machine
5. Après le mot de passe, redirection vers la page de connexion Google officielle
5. Pour le devoir principal, ouvrir aussi `http://localhost:8765/index.html` puis exporter en PDF

## Utilisation sans serveur

Si tu ouvres `login-simulation.html` directement depuis le disque, la requête d'enregistrement échouera. Le message d'erreur t'indiquera de lancer `python server.py`.

## Rappel éthique

Cette page est uniquement une simulation pédagogique locale. Elle ne doit pas être utilisée pour envoyer de vrais e-mails, récupérer des mots de passe ou collecter des données personnelles.
