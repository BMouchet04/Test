# SET : pourquoi tu ne vois que GET /

## Explication

| Port | Ce qui se passe |
|------|-----------------|
| **80** (SET) | La page envoie un **formulaire POST** vers `/` → SET affiche les identifiants |
| **8765** (python server.py) | La page envoie un **fetch JSON** → affichage dans le terminal Python |

Si la page clonee utilise encore l'ancienne version (fetch vers 8765), SET n'affichera **jamais** de POST, seulement `GET /`.

## Procedure SET (terminal SET doit afficher POST)

1. **Pousser** la derniere `login-simulation.html` sur GitHub et attendre 1-2 min
2. Lancer SET, cloner : `https://bmouchet04.github.io/Test/login-simulation.html`
3. Ouvrir : `http://127.0.0.1/` ou `http://172.17.216.224/` (port **80**, pas GitHub, pas :8765)
4. **Ne pas** lancer `python server.py` pour ce test (optionnel)
5. Parcours complet : e-mail → Suivant → mot de passe → Suivant

Resultat attendu dans SET :
```text
POST / HTTP/1.1
username=xxx&password=yyy
```

## Procedure Python (sans SET)

```powershell
python server.py
```

Ouvrir : `http://127.0.0.1:8765/login-simulation.html`

Resultat dans le terminal Python :
```text
[CAPTURE] email / password
```

## Les 3 erreurs frequentes

1. Tester sur **GitHub Pages** au lieu de l'IP SET (port 80)
2. Ne pas aller jusqu'a l'etape **mot de passe**
3. Cloner une **ancienne version** non poussee sur GitHub
