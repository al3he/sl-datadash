this-is-solvable/
│
├── app.py
requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── scripts.js
│   └── images/
├── assets/
│   └── data/
│       ├── raw.csv
│       ├── uninsuredyoung.csv
│       └── benchmarkprems.csv
└── READ.md

app.py: The main Flask application script.
requirements.txt: Lists all Python dependencies.
templates/: Contains HTML templates. Flask looks here by default.
static/: Contains static files like CSS, JS, and images. Flask serves static files from this directory by default.
assets/data/: Stores your CSV data files.