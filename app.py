
from flask import Flask, jsonify, send_from_directory
import sqlite3, math, webbrowser, threading

app = Flask(__name__)

def compute_utilitarian_score(player):
    PI = player['performance_index']
    UW = math.log(1 + player['resource_gap'])
    SI = player['stage_importance']
    EF = 1 - player['ethical_penalty']
    return round(PI * UW * SI * EF, 2)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect("sports.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = [dict(ix) for ix in cur.fetchall()]
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/api/players/<sport>")
def get_players(sport):
    players = query_db("SELECT * FROM players WHERE sport=?", [sport])
    for p in players:
        p["utilitarian_score"] = compute_utilitarian_score(p)
    return jsonify(players)

@app.route("/api/top/<sport>")
def get_top(sport):
    players = query_db("SELECT * FROM players WHERE sport=?", [sport])
    for p in players:
        p["utilitarian_score"] = compute_utilitarian_score(p)
    players = sorted(players, key=lambda x: x["utilitarian_score"], reverse=True)[:10]
    return jsonify(players)

@app.route("/api/player/<int:player_id>")
def get_player(player_id):
    player = query_db("SELECT * FROM players WHERE id=?", [player_id], one=True)
    if player:
        player["utilitarian_score"] = compute_utilitarian_score(player)
    return jsonify(player)

@app.route("/dashboard")
def dashboard():
    return send_from_directory(".", "utilitarian_classified.html")

def open_browser():
    webbrowser.open("http://127.0.0.1:5000/dashboard")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run()
