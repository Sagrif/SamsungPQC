from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
import time
import math
from services.messaging import send_secure_message
from services.ai_assistant import ask_bixby
from dashboard.security import get_security_info

app = Flask(__name__)

# Simulated Smart Stock Predictions
stock_history = {
    "Apple": [],
    "Amazon": [],
    "Samsung": []
}

def generate_smart_price(company, t):
    base = {
        "Apple": 150,
        "Amazon": 120,
        "Samsung": 90
    }[company]

    if company == "Apple":
        return round(base + 0.5 * t + math.sin(t / 2) * 2, 2)
    elif company == "Amazon":
        return round(base + math.sin(t / 1.5) * 3 + (t % 5) * 0.1, 2)
    elif company == "Samsung":
        return round(base + 5 * math.sin(t / 3) + math.cos(t / 2) * 2, 2)

@app.route("/api/stock_data")
def stock_data():
    t = int(time.time() % 100)
    for company in stock_history:
        new_price = generate_smart_price(company, t)
        stock_history[company].append(new_price)
        if len(stock_history[company]) > 15:
            stock_history[company].pop(0)
    return jsonify(stock_history)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/messaging", methods=["GET", "POST"])
def messaging():
    if request.method == "POST":
        to = request.form["to"]
        msg = request.form["message"]
        send_secure_message(to, msg)
        return redirect(url_for("messaging"))
    return render_template("messaging.html")

@app.route("/bixby", methods=["GET", "POST"])
def bixby():
    response = None
    if request.method == "POST":
        query = request.form["query"]
        response = ask_bixby(query)
    return render_template("bixby.html", response=response)

@app.route("/dashboard")
def dashboard():
    data = get_security_info()
    return render_template("dashboard.html", data=data)

@app.route("/announcements", methods=["GET", "POST"])
def announcements():
    announcements = []
    if os.path.exists("data/announcements.json"):
        with open("data/announcements.json", "r") as f:
            announcements = json.load(f)

    if request.method == "POST":
        new_announcement = request.form["announcement"]
        announcements.insert(0, new_announcement)
        with open("data/announcements.json", "w") as f:
            json.dump(announcements, f, indent=2)

    return render_template("announcements.html", announcements=announcements)

@app.route("/trade_hub", methods=["GET", "POST"])
def trade_hub():
    result = None
    if request.method == "POST":
        buyer = request.form["buyer"]
        seller = request.form["seller"]
        item = request.form["item"]
        result = f"🔐 Secure Trade Confirmed: {buyer} bought {item} from {seller}."
    return render_template("trade_hub.html", result=result)

@app.route("/stock_tracker")
def stock_tracker():
    return render_template("stock_tracker.html")

if __name__ == "__main__":
    app.run(debug=True)
