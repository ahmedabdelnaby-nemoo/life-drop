# Life Drop - Blood Donation Management System

A robust and user-friendly web application designed to connect blood donors with individuals or institutions in need. Built using **Python** and **Flask**, this platform streamlines the donor registration process, manages records efficiently using **SQLite**, and features data persistence for forms.

## Live Demo

**GitHub Repository:** [github.com/a01145389704-spec/life-drop](https://github.com/a01145389704-spec/life-drop)

Deploy on [Railway](https://railway.app) using the included `Procfile` and `railway.toml`, then add your live URL here.

## Features

- **Donor Registration & Management:** Register blood donors with personal details, contact info, and blood type.
- **Form Data Persistence:** `localStorage` in `donors.html` saves registration drafts automatically so data is not lost on page refresh.
- **Database Management:** **SQLite** for secure, structured backend storage.
- **Responsive UI:** Clean HTML templates optimized for a smooth user experience.

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript (`localStorage` draft saving)
- **Deployment:** Gunicorn, Railway

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/a01145389704-spec/life-drop.git
cd life-drop
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Routes

| Route | Description |
|-------|-------------|
| `/` | Splash screen, then redirects to donor registration |
| `/index` | Main landing page |
| `/donors?from=splash` | Donor registration form |
| `/save` | POST — save donor to SQLite |
| `/show` | View all registered donors |
| `/success` | Registration confirmation (via `/save`) |

## License

Open source — for personal and educational use.
