import requests
import mysql.connector


class Categories_request:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/categories.json"
        self.cat_list = []

    def request_cat(self):
        self.req = requests.get(self.url)
        self.data = self.req.json()
        for i in range(20):
            self.cat_list.append(self.data["tags"][i].get("name"))
        return self.cat_list

    def fill_db(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                for x in self.request_cat():
                    cursor.execute(f"""INSERT INTO categories (name) VALUES ("{x}")""")
                connection.commit()
            except:
                connection.rollback()

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            connection.close()

    def get_cat(self):
        cat_list = []
        try:
            connection = mysql.connector.connect(host="localhost",
                                                      user="flynz",
                                                      password="openfoodfacts",
                                                      database="pur_beurre",
                                                      auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                cursor.execute("""SELECT name FROM categories""")
                rows = cursor.fetchall()
                for row in rows:
                    cat_list.append(row[0])
            except:
                connection.rollback()

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            connection.close()
        return cat_list


class Products_request:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&json=true"
        self.req = requests.get(self.url)
        self.data = self.req.json()
        self.products_name_list = []
        self.products_code_list = []
        self.call_products()
        self.lists_to_dicts()

    def fill_db(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                      user="flynz",
                                                      password="openfoodfacts",
                                                      database="pur_beurre",
                                                      auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                for x in range(20):
                    name = self.data["products"][x].get("generic_name_fr")
                    barcode = self.data["products"][x].get("code")
                    url = self.data["products"][x].get("url")
                    nutrition_grade = self.data["products"][x].get("nutriscore_grade")
                    cursor.execute(
                        f"""INSERT INTO products (name, barcode, url, nutrition_grade) VALUES ("{name}", "{barcode}", "{url}", "{nutrition_grade}")""")
                connection.commit()
            except:
                connection.rollback()

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            connection.close()

    def call_products(self):

        try:
            connection = mysql.connector.connect(host="localhost",
                                                      user="flynz",
                                                      password="openfoodfacts",
                                                      database="pur_beurre",
                                                      auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                cursor.execute("""SELECT name FROM products""")
                rows = cursor.fetchall()
                for row in rows:
                    self.products_name_list.append(row[0])
                cursor.execute("""SELECT barcode FROM products""")
                rows = cursor.fetchall()
                for row in rows:
                    self.products_code_list.append(row[0])
            except:
                connection.rollback()

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            connection.close()

    def lists_to_dicts(self):
        if len(self.products_name_list) != len(self.products_code_list):
            print("PROBLEME LIST_TO_DICT")
        else:
            product_name_code = {}
            for i in range(len(self.products_name_list)):
                product_name_code[self.products_name_list[i]] = self.products_code_list[i]
            return product_name_code
