# reused general implementation from finance in order to have a running front end
import os
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
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
        change = predicted_change(username)
        new_price = recent_price()[0] + change
        #input to tweet thing
        #interpret result and show
        return render_template("result.html", username = username, change = change, new_price=new_price)
    else:
        return redirect("google.com")
        
