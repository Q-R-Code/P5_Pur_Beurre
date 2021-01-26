from Pur_Beurre_P5.off_categories import Categories_request
from create_db import Categories as Cat, db

categories_request = Categories_request().get_cat()

found_cat = Cat.query.first()

print(type(categories_request))