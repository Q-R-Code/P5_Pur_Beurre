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
    image_url = db.Column("image_url", db.String(1000))
    nutrition_grade = db.Column("nutrition_grade", db.String(500))
    image_nutrition = db.Column("image_nutrition", db.String(1000))
    stores = db.Column("stores", db.String(500))


    def __init__(self, id, name, barcode, url, nutrition_grade):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.url = url
        self.nutrition_grade = nutrition_grade


def create_tables():
    db.drop_all()
    db.create_all()

