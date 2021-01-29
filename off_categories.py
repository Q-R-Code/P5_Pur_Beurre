import requests
import mysql.connector


class Categories_request:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/categories.json"
        self.req = requests.get(self.url)
        self.data = self.req.json()
        self.cat_list_test = []

    def request_cat(self):
        for i in range(20):
            self.cat_list_test.append(self.data["tags"][i].get("name"))
        return self.cat_list_test

    def fill_db(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            print("CONNECTION OKAY")

            try:
                for x in self.request_cat():
                    cursor.execute(f"""INSERT INTO categories (name) VALUES ("{x}")""")
                connection.commit()
                print("OKAY")
            except:
                connection.rollback()
                print("NOP")

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        finally:
            connection.close()
            print("CLOSE")

    def get_cat(self):
        cat_list = []
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            print("CONNECTION OKAY")
            try:
                cursor.execute("""SELECT name FROM categories""")
                rows = cursor.fetchall()
                for row in rows:
                    cat_list.append(row)
            except:
                connection.rollback()
                print("NOP")

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        finally:
            connection.close()
            print("CLOSE")

        return cat_list


class Products_request:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&json=true"
        self.req = requests.get(self.url)
        self.data = self.req.json()

    def fill_db(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            print("CONNECTION OKAY")

            try:
                for x in range(20):
                    name = self.data["products"][x].get("generic_name_fr")
                    barcode = self.data["products"][x].get("code")
                    url = self.data["products"][x].get("url")
                    nutrition_grade = self.data["products"][x].get("nutriscore_grade")
                    cursor.execute(
                        f"""INSERT INTO products (name, barcode, url, nutrition_grade) VALUES ("{name}", "{barcode}", "{url}", "{nutrition_grade}")""")
                connection.commit()
                print("OKAY")
            except:
                connection.rollback()
                print("NOP")

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        finally:
            connection.close()
            print("CLOSE")

    def get_products(self):
        products_list = []
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            print("CONNECTION OKAY")
            try:
                cursor.execute("""SELECT name FROM products""")
                rows = cursor.fetchall()
                for row in rows:
                    products_list.append(row)
            except:
                connection.rollback()
                print("NOP")

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

        finally:
            connection.close()
            print("CLOSE")

        return products_list
