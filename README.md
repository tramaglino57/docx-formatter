# SLS Studio Legale — Document Formatter

App web per formattare documenti .docx seguendo lo stile di un modello.

## Come funziona

1. **Step 1**: Carica un file .docx come modello (lo stile da copiare)
2. **Step 2**: Carica il file .docx da formattare
3. **Step 3**: Scarica il documento formattato

## Setup locale

```bash
# 1. Clona il repository
git clone https://github.com/TUO-USERNAME/docx-formatter.git
cd docx-formatter

# 2. Crea un virtual environment
python3 -m venv venv
source venv/bin/activate  # su Windows: venv\Scripts\activate

# 3. Installa le dipendenze
pip install -r requirements.txt

# 4. Avvia l'app
python app.py
```

Apri il browser su http://localhost:5000

## Deploy su Render (gratuito)

1. Vai su https://render.com e crea un account
2. Clicca "New" → "Web Service"
3. Collega il tuo repository GitHub
4. Impostazioni:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Clicca "Create Web Service"

L'app sarà disponibile su un URL tipo: `https://docx-formatter.onrender.com`

## Struttura progetto

```
docx-formatter/
├── app.py              # Backend Flask
├── requirements.txt    # Dipendenze Python
├── Procfile           # Per deploy
├── .gitignore
├── templates/
│   └── index.html     # Frontend
├── uploads/           # File caricati (temporanei)
└── outputs/           # File generati
```

## Prossimi sviluppi

- [ ] Integrazione AI (Claude API) per interpretazione intelligente del contenuto
- [ ] Supporto stili complessi (elenchi, note a piè pagina)
- [ ] Anteprima del documento prima del download
