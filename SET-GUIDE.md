# SET Credential Harvester — guide rapide

## Erreur dans ta config SET

Tu as saisi : `127.0;0.1` (point-virgule) au lieu de `127.0.0.1` (points).

Utilise :
- **`127.0.0.1`** si tu testes sur la meme machine que SET
- **`172.17.216.224`** si tu testes depuis une autre machine (IP affichee par SET/WSL)

## Pourquoi seulement GET / ?

SET reecrit les formulaires au moment du **clone**. La page en 2 etapes (`login-simulation.html` + JavaScript) ne convient souvent pas.

**Solution :** cloner la page simple avec formulaire standard :

```
https://bmouchet04.github.io/Test/login-harvester.html
```

Cette page a `username` + `password` visibles et `method="POST"` `action="/"` sans JavaScript.

## Procedure

1. Pousser sur GitHub : `login-harvester.html` (+ CSS)
2. Arreter SET (Ctrl+C)
3. Vider le clone : `sudo rm -rf /var/www/html/*`
4. Relancer SET → Credential Harvester
5. IP : `127.0.0.1` ou `172.17.216.224` (sans faute de frappe)
6. URL a cloner : `https://bmouchet04.github.io/Test/login-harvester.html`
7. Ouvrir `http://127.0.0.1/` dans le navigateur
8. Remplir e-mail + mot de passe → **Suivant**

Resultat attendu dans SET :

```text
POST / HTTP/1.1
username=...&password=...
```

## Alternative : IMPORT

Si le clone echoue encore :

1. Copier `login-harvester.html` dans le dossier d'import SET
2. Choisir **IMPORT** au lieu de cloner une URL

## Python (sans SET)

```powershell
python server.py
```

→ `http://127.0.0.1:8765/login-simulation.html` (version 2 etapes + API JSON)

Identifiants fictifs uniquement pour le devoir.
