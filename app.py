from flask import Flask, render_template, request, redirect, url_for
from services.messaging import send_secure_message
from services.ai_assistant import ask_bixby
from dashboard.security import get_security_info

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
