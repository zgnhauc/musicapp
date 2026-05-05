# Music Platform — IS218 Group Project

**Team:** Josue Ortiz, Ambrose Mcahee, Annie Nguyen, Julia Navarro, Slobodan Malinkov

---

## Setup (Linux / WSL)

```bash
# 1. Clone the repo and enter the project
git clone <repo-url>
cd musicapp

# 2. Create and activate virtual environment
sudo apt install python3.12-venv   # only needed once on a fresh machine
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python3 manage.py migrate

# 5. Create an admin account (for /admin panel)
python3 manage.py createsuperuser

# 6. Run the server
python3 manage.py runserver
```

Open your browser at `http://127.0.0.1:8000`

---

## Setup (Windows)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Project Structure

```
musicapp/
├── music/                  # Main app — models, views, templates
│   ├── models.py           # Song, Rating, ListeningHistory, LogMessage
│   ├── views.py            # Page logic (home, songs, song detail, about)
│   ├── admin.py            # Admin panel registration
│   └── templates/music/    # Song listing and detail templates
├── musicplatform/          # Project config
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
│   └── templates/          # Base layout, home, about templates
├── manage.py
├── requirements.txt
└── db.sqlite3              # SQLite database (auto-created)
```

---

## Pages

| URL | Description |
|-----|-------------|
| `/` | Home page with log messages |
| `/about/` | About page |
| `/songs/` | Browse all songs |
| `/songs/<id>/` | Song detail + leave a review |
| `/admin/` | Admin panel (requires superuser account) |

---

## Daily Workflow

```bash
# Activate environment every time you open a new terminal
source venv/bin/activate        # Linux/WSL
venv\Scripts\activate           # Windows

# After pulling new changes that include model edits
python3 manage.py migrate

# After editing models yourself
python3 manage.py makemigrations
python3 manage.py migrate
```

---

## Notes

- `venv/` is gitignored — every teammate must create their own locally
- `db.sqlite3` is local — use the admin panel to add test data
- Always activate the virtual environment before running any `manage.py` command
