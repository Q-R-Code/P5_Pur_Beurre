from flask import Flask, redirect, url_for, render_template, request, session, flash
from off_categories import Categories_request, fill_bd
from create_db import *
import pymysql

app = Flask(__name__)
app.secret_key = "admin"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://flynz:openfoodfacts@localhost/pur_beurre'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/")
def home():
    return render_template("home.html", cat=Categories_request().get_cat())


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    create_tables()
    fill_bd()
    app.run(debug=True)
