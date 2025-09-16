
# Utilitarian Talent Selector (EXE Build)

This bundle contains:
- app.py (Flask backend with Utilitarian Score computation)
- sports.db (SQLite database of mock professional players)
- utilitarian_classified.html (frontend dashboard with classifications)

## How to Build a Standalone EXE

1. Install dependencies:
   pip install flask pyinstaller

2. Open a terminal in this folder.

3. Build the exe:
   pyinstaller --onefile --add-data "sports.db;." --add-data "utilitarian_classified.html;." app.py

   (On Linux/Mac replace ';' with ':')

4. After building, the EXE will be inside the 'dist' folder as 'app.exe'.

5. Run 'app.exe' → it will start the server and auto-open your browser at:
   http://127.0.0.1:5000/dashboard
