"""
The main module of this app. Launch Flask, initializes the different routes.

"""

import ast
import sys

from flask import Flask, render_template, request, flash, url_for, redirect

from app.substitute_in_db import Sub_to_save, My_substitutes, Sub_to_delete
from app.cat_products_popular import Categories_request, Products_request
from app.create_db import *
from app.search_product import Search_barcode, call_api_test, Search_substitutes

app = Flask(__name__)
app.secret_key = "admin"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://flynz:openfoodfacts@localhost/pur_beurre'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False



@app.route("/", methods=["POST", "GET"])
def home():
    """
    This is the main route of the program, "home.html"
    Generates popular categories and products.

    """
    return render_template("home.html", cat=Categories_request().get_cat(),
                           prod_name=Products_request().lists_to_dicts())


@app.route("/products", methods=["POST", "GET"])
def products():
    """
    This route is called when a user searches with a barcode.
    - Calls the API , check if it responds and returns the "products.html" page with the desired product
    and its substitutes.

    """
    global products_data
    if request.method == "POST":
        barcode = request.form["barcode"]
        if call_api_test(barcode) == 1:
            name = Search_barcode(barcode).get_name()
            url = Search_barcode(barcode).get_url()
            image = Search_barcode(barcode).get_image()
            image_nutrition = Search_barcode(barcode).get_image_nutrition()
            nutriscore = Search_barcode(barcode).get_nutriscore()
            substitutes = Search_substitutes(barcode).get_list_better()
            sub_none = False
            if len(substitutes) == 0:
                sub_none = True
            products_data = {"name": name, "url": url, "image": image, "image_nutrition": image_nutrition,
                             "nutriscore": nutriscore, "substitutes": substitutes, "sub_none" : sub_none}
            return render_template("products.html",  name=name, url=url, image=image, image_nutrition=image_nutrition,
                                   nutriscore=nutriscore, sub=substitutes, sub_none=sub_none)
        else:
            products_data = {}
            flash("Code barre (EAN) incorrect!")
            return redirect(url_for("home"))
    else:
        products_data = {}
        return redirect(url_for("home"))


@app.route("/product_to_save", methods=["POST", "GET"])
def product_to_save():
    """
    When a user wants to register a substitute with the button, call this route.
    redirect to "my_products.html" page.

    """
    if request.method == "POST":
        product = request.form["product"]
        product = ast.literal_eval(product)
        Sub_to_save(product)
        return render_template("products.html", name=products_data["name"], url=products_data["url"], image=products_data["image"], image_nutrition=products_data["image_nutrition"],
                                   nutriscore=products_data["nutriscore"], sub=products_data["substitutes"], sub_none=products_data["sub_none"])

    else:
        return redirect(request.referrer)


@app.route("/product_to_delete", methods=["POST", "GET"])
def product_to_delete():
    """
    When the button "supprimer" in my_products.html,  call this route to delete the substitute.

    """
    if request.method == "POST":
        product = request.form["product"]
        product = ast.literal_eval(product)
        Sub_to_delete(product)
        return redirect("products-saved")
    else:
        return redirect(url_for("home"))


@app.route("/products-saved")
def my_products():
    """
    return the page my_products with the substitutes saved in the table "substitutes_saved".

    """
    products = My_substitutes().get_substitues_saved()
    return render_template("my_products.html", products=products)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        create_tables()
        Categories_request().fill_db()
        Products_request().fill_db()
    app.run(debug=True)
