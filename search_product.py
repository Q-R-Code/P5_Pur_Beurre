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
        self.name = self.data["product"].get("product_name_fr")
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


class Search_substitutes():

    def __init__(self, barcode):
        self.barcode = barcode


    def get_cat(self):
        url = f"https://fr.openfoodfacts.org//api/v0/produit/{self.barcode}"
        req = requests.get(url)
        data= req.json()
        cat_tags_search = []
        for x in data["product"]["categories_hierarchy"]:
            cat_tags_search.append(x[3:])
        return cat_tags_search

    def get_list_better(self):
        cat = self.get_cat()
        url2 = f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={cat[0]}&tagtype_1=categories&tag_contains_1=contains&tag_1={cat[1]}&tagtype_2=categories&tag_contains_2=contains&tag_2={cat[2]}&tagtype_3=categories&tag_contains_3=contains&tag_3={cat[3]}&page_size=100&json=true"
        req2 = requests.get(url2)
        search_better_nutriscore = []
        data2 = req2.json()
        for x in range(100):
            score = data2["products"][x].get("nutriscore_grade")
            if score == str("a"):
                search_better_nutriscore.append(data2["products"][x])
            elif len(search_better_nutriscore) == 5:
                return search_better_nutriscore
        if len(search_better_nutriscore) < 5:
            for x in range(100):
                score = data2["products"][x].get("nutriscore_grade")
                if score == str("b"):
                    search_better_nutriscore.append(data2["products"][x])
                elif len(search_better_nutriscore) == 5:
                    return search_better_nutriscore
        elif len(search_better_nutriscore) < 5:
            for x in range(100):
                score = data2["products"][x].get("nutriscore_grade")
                if score == str("c"):
                    search_better_nutriscore.append(data2["products"][x])
                elif len(search_better_nutriscore) == 5:
                    return search_better_nutriscore
        return search_better_nutriscore

