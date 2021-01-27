import requests

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


