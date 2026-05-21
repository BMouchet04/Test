# Aucune requete POST dans SET — diagnostic

## Test sans SET (obligatoire d'abord)

Verifie que le formulaire HTML fonctionne :

```powershell
cd c:\Users\benja\Desktop\Perso\bruteforce\Test
python test-harvest.py
```

1. Ouvre **http://127.0.0.1:8888/**
2. Remplis e-mail + mot de passe
3. Clique **Suivant**

Dans le terminal tu dois voir :

```text
>>> POST / depuis ...
    username = ...
    password = ...
```

- **Si ca marche** → le HTML est bon, le probleme vient de SET / reseau / config.
- **Si ca ne marche pas** → probleme navigateur (cache, extension).

---

## Config SET correcte

| Champ | Valeur |
|-------|--------|
| IP POST back | `127.0.0.1` (meme PC) ou `172.17.216.224` (WSL) |
| **Pas** | `127.0;0.1` (faute de frappe) |
| URL a cloner | `https://bmouchet04.github.io/Test/` **ou** `.../index.html` |

Utilise **`index.html`** (formulaire minimal a la racine), pas `login-simulation.html`.

---

## Procedure SET (WSL / Kali)

```bash
# 1. Arreter SET (Ctrl+C)

# 2. Vider l'ancien clone
sudo rm -rf /var/www/html/*

# 3. Relancer setoolkit → Credential Harvester

# 4. IP : 127.0.0.1 ou 172.17.216.224

# 5. URL : https://bmouchet04.github.io/Test/

# 6. Dans le navigateur (Windows) :
#    http://127.0.0.1/   OU   http://172.17.216.224/
```

Remplis **les deux champs** puis **Suivant**. Un simple chargement de page = seulement `GET /`.

---

## Causes frequentes (seulement GET)

1. **Pas de clic sur Suivant** apres le mot de passe
2. **Ancien clone** dans `/var/www/html/` → vider et re-cloner
3. **Mauvaise URL** dans le navigateur (GitHub au lieu de l'IP SET)
4. **Port 80** : SET dans WSL, navigateur Windows — essaie `http://172.17.216.224/`
5. **Page en 2 etapes** (`login-simulation.html`) — utiliser **`index.html`**
6. **Fichiers pas pousses** sur GitHub avant le clone

---

## IMPORT (si le clone URL echoue)

Dans SET, choisir **IMPORT** et pointer vers :

```
chemin/vers/index.html
```

sur ta machine (copie le fichier du projet Test).

---

## Python en parallele (optionnel)

```powershell
python server.py
```

→ `http://127.0.0.1:8765/login-simulation.html` (ne remplace pas SET sur le port 80).
