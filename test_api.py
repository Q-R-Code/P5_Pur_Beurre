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
"""

print(data["products"][5].get("product_name"))
print(data["products"][5].get("product_name_fr"))
print(data["products"][5].get("generic_name"))
print(data["products"][5].get("generic_name_fr"))