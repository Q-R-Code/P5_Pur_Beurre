from flask import Flask, render_template, request
from off_categories import Categories_request, Products_request
from create_db import *
from search_product import search_barcode

app = Flask(__name__)
app.secret_key = "admin"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://flynz:openfoodfacts@localhost/pur_beurre'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        barcode = request.form["barcode"]
        search = search_barcode(barcode)
        return render_template("produit.html", barcode=search)
    else:
        return render_template("home.html", cat=Categories_request().get_cat(), prod=Products_request().get_products())

@app.route("/produit")
def produit():
    return render_template("produit.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    create_tables()
    Categories_request().fill_db()
    Products_request().fill_db()
    app.run(debug=True)
