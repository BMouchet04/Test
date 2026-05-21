# Guide SET + page de connexion

## Pourquoi SET ne voit rien

| URL testée | Ce qui se passe |
|------------|-----------------|
| `https://bmouchet04.github.io/Test/login-simulation.html` | La page est sur **GitHub**, pas sur SET. Aucune donnée dans le terminal SET. |
| `http://localhost:8765/...` + `python server.py` | Enregistrement **JSON** vers ton serveur Python. SET (port **80**) ne reçoit rien. |
| `http://172.17.216.224/` (IP SET, port **80**) | **C'est la bonne URL** pour le harvester. |

Les requêtes JSON `{email, password, date}` viennent du mode **python server.py**, pas de SET.

## Procédure correcte

1. **Arrêter** `python server.py` (libère le port si besoin, évite la confusion).
2. Lancer SET → Credential Harvester → cloner :
   `https://bmouchet04.github.io/Test/login-simulation.html`
3. **Pousser** la dernière version de `login-simulation.html` sur GitHub avant de cloner.
4. Ouvrir dans le navigateur : **`http://172.17.216.224/`** (ton IP SET), **pas** l'URL GitHub.
5. Parcours : e-mail → Suivant → mot de passe → Suivant.
6. Dans le terminal SET, tu dois voir un **POST /** avec `username` et `password`.

## Champs reconnus par SET

- `username` = e-mail saisi
- `password` = mot de passe

Formulaire HTML : `method="POST"` `action="/"`.

## Test local sans SET

```powershell
python server.py
```

Ouvrir : `http://localhost:8765/login-simulation.html`  
→ enregistrement JSON dans `captures.json` puis redirection Google.
