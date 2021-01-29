import requests
import mysql.connector


class Categories_request:

    def __init__(self):
        self.url = "https://fr.openfoodfacts.org/categories.json"
        self.req = requests.get(self.url)
        self.data = self.req.json()
        #self.cat_list = set()
        self.cat_list_test = []

    def get_cat(self):
        for i in range(20):
            # self.cat_list.add(self.data["tags"][i].get("name"))
            self.cat_list_test.append(self.data["tags"][i].get("name"))
        # return self.cat_list
        return self.cat_list_test

#https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&json=true


def fill_db():

    cat = Categories_request()

    try:
        connection = mysql.connector.connect(host="localhost",
                                             user="flynz",
                                             password="openfoodfacts",
                                             database="pur_beurre",
                                             auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        print("CONNECTION OKAY")

        try:
            for x in cat.get_cat():
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

