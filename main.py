from flask import Flask, render_template, request, flash, url_for, redirect
from off_categories import Categories_request, Products_request
from create_db import *
from search_product import Search_barcode, call_api_test, Search_substitutes

app = Flask(__name__)
app.secret_key = "admin"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://flynz:openfoodfacts@localhost/pur_beurre'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html", cat=Categories_request().get_cat(),
                            prod_name=Products_request().lists_to_dicts())

@app.route("/products", methods=["POST", "GET"])
def products():
    if request.method == "POST":
        barcode = request.form["barcode"]
        if call_api_test(barcode) == 1:
            name = Search_barcode().get_name(barcode)
            url = Search_barcode().get_url(barcode)
            image = Search_barcode().get_image(barcode)
            image_nutrition = Search_barcode().get_image_nutrition(barcode)
            nutriscore = Search_barcode().get_nutriscore(barcode)
            substitutes = Search_substitutes(barcode).get_list_better()
            sub_none = False
            if len(substitutes) == 0:
                sub_none= True
            return render_template("products.html", name=name, url=url, image=image, image_nutrition=image_nutrition,
                                    nutriscore=nutriscore, sub=substitutes, sub_none=sub_none)
        else:
            flash("Code barre (EAN) incorrect!")
            return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

@app.route("/products-saved")
def my_products():
    return render_template("products-saved.html")


if __name__ == "__main__":
    create_tables()
    Categories_request().fill_db()
    Products_request().fill_db()
    app.run(debug=True)
