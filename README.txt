
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

## Android App (Judge Your Bias)

A native Android wrapper for the game is included in `android-app/`.

### Open in Android Studio
1. Open Android Studio.
2. Choose **Open** and select the `android-app` folder.
3. Let Gradle sync.
4. Run on an emulator/device.

The app launches a WebView that loads:
`file:///android_asset/judge_your_bias.html`

To refresh game content, copy the root file into assets:
`cp judge_your_bias.html android-app/app/src/main/assets/judge_your_bias.html`
