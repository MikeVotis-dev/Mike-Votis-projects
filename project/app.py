from flask import Flask, render_template, request, redirect, session
from cs50 import SQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "super_secret_project_key"

db = SQL("sqlite:///finance.db")

@app.route("/")
def index():
    if "user_id" not in session:
        return redirect("/login")

    history = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])
    return render_template("index.html", transactions=history)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("username")
        pwd = request.form.get("password")

        if not name or not pwd:
            return "Missing info", 400

        hashed_pwd = generate_password_hash(pwd)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, hashed_pwd)
            return redirect("/login")
        except ValueError:
            return "Username taken", 400

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        name = request.form.get("username")
        pwd = request.form.get("password")

        user_data = db.execute("SELECT * FROM users WHERE username = ?", name)

        if len(user_data) != 1 or not check_password_hash(user_data[0]["hash"], pwd):
            return "Invalid credentials", 403

        session["user_id"] = user_data[0]["id"]
        return redirect("/")

    return render_template("login.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        action_type = request.form.get("type")
        category = request.form.get("category")
        cash = request.form.get("amount")

        db.execute("INSERT INTO transactions (user_id, type, category, amount) VALUES (?, ?, ?, ?)",
                   session["user_id"], action_type, category, cash)
        return redirect("/")

    return render_template("add.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
