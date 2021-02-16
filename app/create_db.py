"""
This module use SQLAlchemy for create the different tables at the first launch.
* Categories & Products : for the home page.
* Substitutes_saved : To save the substitutes and find them in "mes produits".

"""

from flask_sqlalchemy import SQLAlchemy

from main import app

db = SQLAlchemy(app)


class Categories(db.Model):
    id = db.Column("Id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(500))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Products(db.Model):
    id = db.Column("Id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(500))
    barcode = db.Column("barcode", db.String(500))
    url = db.Column("url", db.String(500))
    nutrition_grade = db.Column("nutrition_grade", db.String(500))


    def __init__(self, id, name, barcode, url, nutrition_grade):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.url = url
        self.nutrition_grade = nutrition_grade

class Substitutes_saved(db.Model):
    id = db.Column("Id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(500))
    url = db.Column("url", db.String(500))
    image_url = db.Column("image_url", db.String(500))
    nutrition_grade = db.Column("nutrition_grade", db.String(500))
    image_nutrition = db.Column("image_nutrition", db.String(500))
    stores = db.Column("stores", db.String(500))


    def __init__(self, id, name, barcode, url, nutrition_grade):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.url = url
        self.nutrition_grade = nutrition_grade


def create_tables():
    """
    This fonction is called when the user writes : "main.py init" at the launch
    Drop all tables and recreate them. Can be useful for updating popular categories and products on the home page.

    """
    db.drop_all()
    db.create_all()

