from flask import Flask, render_template, request, flash, url_for, redirect
from off_categories import Categories_request, Products_request
from create_db import *
from search_product import Search_barcode, call_api_test

app = Flask(__name__)
app.secret_key = "admin"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://flynz:openfoodfacts@localhost/pur_beurre'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        barcode = request.form["barcode"]
        if call_api_test(barcode) == 1:
            name = Search_barcode().get_name(barcode)
            url = Search_barcode().get_url(barcode)
            image = Search_barcode().get_image(barcode)
            image_nutrition = Search_barcode().get_image_nutrition(barcode)
            nutriscore = Search_barcode().get_nutriscore(barcode)
            return render_template("products.html", name=name, url=url, image=image, image_nutrition=image_nutrition,
                                nutriscore=nutriscore)

        else:
            flash("Code barre (EAN) incorrect!")
            return redirect(url_for("home"))
    else:
        return render_template("home.html", cat=Categories_request().get_cat(),
                               prod_name=Products_request().lists_to_dicts())


@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/products-saved")
def my_products():
    return render_template("products-saved.html")


if __name__ == "__main__":
    create_tables()
    Categories_request().fill_db()
    Products_request().fill_db()
    app.run(debug=True)
