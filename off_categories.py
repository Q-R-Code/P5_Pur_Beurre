import requests



class Categories:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/categories.json"
        self.req = requests.get(self.url)
        self.data = self.req.json()
        self.cat_list = set()
        self.cat_list_test = {}

    def get_cat(self):
        for i in range(20):
            self.cat_list.add(self.data["tags"][i].get("name"))
        return self.cat_list




class Products:

    def __init__(self):
        self.req = requests.get(
            "https://fr.openfoodfacts.org/cgi/search.pl?action=process&unique_scans_n&page=1&json=true")
        self.data = self.req.json()
        self.product = {}
        self.product_name_url = []

    def get_products(self):
        for i in range(20):
            name = self.data["products"][i].get("product_name")
            url = self.data["products"][i].get("url")
            self.product["name"] = name
            self.product["url"] = url
            self.product_name_url.append(self.product)


"""
prod = Products()
prod.get_products()


for x in Categories().get_cat():
    print(x)
print(type(data))
print(data.keys())
print(type(data["products"][0]))


req = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&unique_scans_n&page=1&json=true")
data = req.json()
for i in range(20):
    name = data["products"][i].get("product_name")
    url = data["products"][i].get("url")
    print("Le nom est : {} et l'url est : {}".format(name, url))
"""
