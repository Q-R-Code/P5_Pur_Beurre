import requests


def search_barcode(barcode):
    url = f"https://fr.openfoodfacts.org//api/v0/produit/{barcode}"
    req = requests.get(url)
    data = req.json()
    return_data = []
    return_data.append(data["product"].get("product_name"))
    return return_data