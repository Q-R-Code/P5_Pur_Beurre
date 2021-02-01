import requests

"""
def search_barcode(barcode):
    url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
    req = requests.get(url)
    data = req.json()
    return_data = []
    return_data.append(data["product"].get("product_name"))
    return return_data

"""

class Search_barcode():

    def __init__(self):
        self.barcode = None
        self.name = None
        self.nutriscore = None
        self.url = None
        self.image = None
        self.substitus = None
        self.store = None
        self.data = None
        self.return_data = []

    def get_name(self, barcode):
        url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
        req = requests.get(url)
        self.data = req.json()
        self.name = self.data["product"].get("product_name")
        return self.name

    def get_url(self, barcode):
        url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
        req = requests.get(url)
        self.data = req.json()
        self.url = "https://fr.openfoodfacts.org/produit/{}".format(self.data["product"].get("code"))
        print(self.url)
        return self.url

