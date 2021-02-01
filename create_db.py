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
    id_categorie = db.Column("id_categorie", db.Integer)

    def __init__(self, id, name, barcode, url, nutrition_grade, id_categorie):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.url = url
        self.nutrition_grade = nutrition_grade
        self.id_categorie = id_categorie

def create_tables():
    db.drop_all()
    db.create_all()

