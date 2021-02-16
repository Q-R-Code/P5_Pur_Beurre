"""
This module is for the function search on the home page.
call_api_test : check if the api responds and return the status.
Search_barcode : for the product that is search
Search_substitutes : Search for up to 5 substitutes with a good nutriscore

"""

import requests


def call_api_test(barcode):
    url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
    req = requests.get(url)
    data = req.json()
    return data["status"]


class Search_barcode():

    def __init__(self, barcode):
        self.barcode = barcode
        self.name = None
        self.nutriscore = None
        self.url = None
        self.image = None
        self.image_nutrition = None
        self.substitute = None
        self.store_substitute = None
        self.data = None
        self.get_data()

    def get_data(self):
        url = f"https://fr.openfoodfacts.org//api/v0/produit/{self.barcode}"
        req = requests.get(url)
        self.data = req.json()
        self.name = self.data["product"].get("product_name_fr")
        self.url = "https://fr.openfoodfacts.org/produit/{}".format(self.data["product"].get("code"))
        self.image = self.data["product"].get("image_url")
        self.image_nutrition = self.data["product"].get("image_nutrition_url")
        self.nutriscore = self.data["product"].get("nutriscore_grade")

    def get_name(self):
        return self.name

    def get_url(self):
        return self.url

    def get_image(self):
        return self.image

    def get_image_nutrition(self):
        return self.image_nutrition

    def get_nutriscore(self):
        return self.nutriscore


class Search_substitutes():

    def __init__(self, barcode):
        self.barcode = barcode

    def get_cat(self) -> list:
        """
        get catégories and return a list.

        """
        url = f"https://fr.openfoodfacts.org//api/v0/produit/{self.barcode}"
        req = requests.get(url)
        data = req.json()
        cat_tags_search = []
        for x in data["product"]["categories_hierarchy"]:
            cat_tags_search.append(x[3:])
            if len(cat_tags_search) == 4:
                return cat_tags_search
        return cat_tags_search

    def get_list_better(self) ->list:
        """
        To have similar products, I decided to do an API search with max 4 catégories.
        Return a list of 100 products.
        For each of them, we check if the nutriscore is "a".
        If the list contains 5 substitutes, stop and returns it.
        If not, same process with the nutriscore "b".
        if there are still not 5 substitutes, we search nutriscore "c" and that's all.
        I consider that the other nutriscore are not good.

        """
        cats = self.get_cat()
        url2 = f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&"
        for i in range(len(cats)):
            url2 += f"tagtype_{i}=categories&tag_contains_{i}=contains&tag_{i}={cats[i]}&"
        url2 += "page_size=100&json=true"
        req2 = requests.get(url2)
        search_better_nutriscore = []
        data2 = req2.json()
        for x in range(100):
            score = data2["products"][x].get("nutriscore_grade")
            if score == str("a") and len(search_better_nutriscore) < 5:
                search_better_nutriscore.append(data2["products"][x])
            elif len(search_better_nutriscore) == 5:
                return search_better_nutriscore
        if len(search_better_nutriscore) < 5:
            for x in range(100):
                score = data2["products"][x].get("nutriscore_grade")
                if score == str("b") and len(search_better_nutriscore) < 5:
                    search_better_nutriscore.append(data2["products"][x])
                elif len(search_better_nutriscore) == 5:
                    return search_better_nutriscore
        elif len(search_better_nutriscore) < 5:
            for x in range(100):
                score = data2["products"][x].get("nutriscore_grade")
                if score == str("c") and len(search_better_nutriscore) < 5:
                    search_better_nutriscore.append(data2["products"][x])
                elif len(search_better_nutriscore) == 5:
                    return search_better_nutriscore
        return search_better_nutriscore
