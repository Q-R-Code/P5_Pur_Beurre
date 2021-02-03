import requests


def call_api_test(barcode):
    url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
    req = requests.get(url)
    data = req.json()
    return data["status"]




class Search_barcode():

    def __init__(self):
        self.barcode = None
        self.name = None
        self.nutriscore = None
        self.url = None
        self.image = None
        self.image_nutrition = None
        self.substitute = None
        self.store_substitute = None
        self.data = None
        self.return_data = []

    def connection(self, barcode):
        url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
        req = requests.get(url)
        self.data = req.json()

    def get_name(self, barcode):
        self.connection(barcode)
        self.name = self.data["product"].get("product_name")
        return self.name

    def get_url(self, barcode):
        self.connection(barcode)
        self.url = "https://fr.openfoodfacts.org/produit/{}".format(self.data["product"].get("code"))
        return self.url

    def get_image(self, barcode):
        self.connection(barcode)
        self.image = self.data["product"].get("image_url")
        return self.image

    def get_image_nutrition(self, barcode):
        self.connection(barcode)
        self.image_nutrition = self.data["product"].get("image_nutrition_url")
        return self.image_nutrition

    def get_nutriscore(self, barcode):
        self.connection(barcode)
        self.nutriscore = self.data["product"].get("nutriscore_grade")
        return self.nutriscore


    def get_substitute(self, barcode):
        self.connection(barcode)
        self.substitute = self.data["product"].get("image_url")
        return self.substitute

    def get_store_substitute(self, barcode):
        self.connection(barcode)
        self.image = self.data["product"].get("image_url")
        return self.image




