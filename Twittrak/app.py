# reused general implementation from finance in order to have a running front end
from flask import Flask, redirect, render_template, request
from backend.stock_data import recent_price
from backend.stock_prediction import predicted_change
# short helper to format money from finance pset
def usd(value):
    return f"${value:,.2f}"
# Configure application
app = Flask(__name__)
app.jinja_env.filters["usd"] = usd
# Configure session to use filesystem (instead of signed cookies)
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/correlate", methods=['GET','POST'])
def correlate():
    if request.method == "POST":
        username = request.form.get("username")
        #check if valid username
        for char in username:
            if not char.isnumeric() and not char.isalpha():
                return redirect("/")
        change = predicted_change(username)
        if change == "Invalid Input":
            return redirect("/")
        new_price = recent_price()[0] + change
        #input to tweet thing
        #interpret result and show
        if change > 0:
            return render_template("result.html", username = username, change = change, new_price=new_price)
        if change < 0:
            change = abs(change)
            return render_template("resultbad.html", username = username, change = change, new_price=new_price)
        if change == 0:
            return render_template("noresult.html", username = username, change = change, new_price=new_price)
    else:
        return redirect("/")
@app.route("/home", methods=['GET','POST'])
def home():
    return redirect("/")
