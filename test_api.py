import requests
"""
url = "https://fr.openfoodfacts.org/categories.json"

request = requests.get(url)

data = request.json()

print(data.keys())

print(type(data))
print(type(data["count"]))
print(type(data["tags"]))
print(type(data["tags"][0]))

print("======================================================")
print(data["count"])
print("======================================================")

test_dict = []
for i in range(10):
    print(data["tags"][i])
    test_dict.append(data["tags"][i])

print("=======================================================")
for i in enumerate(test_dict):
    print(i)
print("======================================================")
print(type(test_dict[1]))
print(test_dict[1])
print("======================================================")
for i in test_dict[1].items():
    print(i)
print("======================================================")
print(test_dict[1].get("id"))
print("======================================================")
print(data["tags"][1].get("id"))
print("======================================================")
categories_list = []
for i in range(50):
    categories_list.append(data["tags"][i].get("id"))
print(categories_list)
print("======================================================")

categories_list2 = set()
for i in range(50):
    categories_list2.add(data["tags"][i].get("name"))
print(categories_list2)
"""

url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&json=true"
req= requests.get(url)
data = req.json()


"""
print(type(data))
print(data.keys())
print(type(data["products"]))
print(data["products"][0])

print(data["products"][1].get("product_name"))
print(data["products"][1].get("product_name_fr"))
print(data["products"][1].get("generic_name"))
print(data["products"][1].get("generic_name_fr"))

for x in range(20):
    print(data["products"][x].get("product_name"))
    print(data["products"][x].get("generic_name_fr"))


"code"
"nutriscore_data"
"nutriscore_grade"
"url"

for x in range(5):
    print(data["products"][x].get("product_name"))
    print(data["products"][x].get("code"))
    print(data["products"][x].get("nutriscore_grade"))
    print(data["products"][x].get("url"))
 

print(data["products"][5].get("product_name"))
print(data["products"][5].get("product_name_fr"))
print(data["products"][5].get("generic_name"))
print(data["products"][5].get("generic_name_fr"))

barcode = "nutella"

def call_api_test(barcode):
    url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
    req = requests.get(url)
    data = req.json()
    if data["status"] == 1:
        print("OK")
    else:
        print("nop")
call_api_test(barcode)
"""
#url1 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=plant-based-foods-and-beverages&tagtype_1=categories&tag_contains_1=contains&tag_1=plant-based-foods&tagtype_2=categories&tag_contains_2=contains&tag_2=snacks-sucres&tagtype_3=categories&tag_contains_3=contains&tag_3=cereals-and-potatoes&page_size=100&json=true"
#https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=plant-based-foods-and-beverages&tagtype_1=categories&tag_contains_1=contains&tag_1=plant-based-foods&tagtype_2=categories&tag_contains_2=contains&tag_2=snacks-sucres&tagtype_3=categories&tag_contains_3=contains&tag_3=cereals-and-potatoes



def get_cat():
    url = "https://fr.openfoodfacts.org//api/v0/produit/3017620420009"
    req = requests.get(url)
    data= req.json()
    cat_tags_search = []
    for x in data["product"]["categories_hierarchy"]:
        cat_tags_search.append(x[3:])
    return cat_tags_search

def get_list_better():
    cat = get_cat()
    url2 = f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={cat[0]}&tagtype_1=categories&tag_contains_1=contains&tag_1={cat[1]}&tagtype_2=categories&tag_contains_2=contains&tag_2={cat[2]}&tagtype_3=categories&tag_contains_3=contains&tag_3={cat[3]}&page_size=100&json=true"
    req2 = requests.get(url2)
    search_better_nutriscore = []
    data2 = req2.json()
    for x in range(100):
        score = data2["products"][x].get("nutriscore_grade")
        if score == str("a"):
            search_better_nutriscore.append(data2["products"][x])
    for x in search_better_nutriscore:
        print(x.get("product_name"), "code:", x.get("code"))


get_list_better()
