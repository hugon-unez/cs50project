from flask import Flask, redirect, render_template, request
from backend.stock_data import recent_price
from backend.stock_prediction import predicted_change
# short helper to format money from finance pset
def usd(value):
    return f"${value:,.2f}"

# Configure application
app = Flask(__name__)
app.jinja_env.filters["usd"] = usd

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
        #check if valid username before submitting to API
        for char in username:
            if not char.isnumeric() and not char.isalpha():
                return redirect("/")
        # call predicted_change function to check if API returned a valid username
        change = predicted_change(username)
        if change == "Invalid Input":
            return redirect("/")
        # the predicted price is the most recent price plus the predicted
        new_price = recent_price()[0] + change
        #interpret result and show template
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
