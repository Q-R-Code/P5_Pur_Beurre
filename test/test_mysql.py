import requests
import mysql.connector
"""
req = requests.get("https://fr.openfoodfacts.org/categories.json")

try:
    connection = mysql.connector.connect(host="localhost",
                                         user="flynz",
                                         password="openfoodfacts",
                                         database="openfoodfacts",
                                         auth_plugin='mysql_native_password')

    cursor = connection.cursor()

    try:




    except:
        connection.rollback()

    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except mysql.connector.errors.InterfaceError as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
finally:
    connection.close()

"""

class My_substitutes():

    def __init__(self):
        self.substitutes = []
        self.get_substitues()

    def get_substitues(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                cursor.execute("""SELECT name FROM substitutes_saved WHERE name="Ama" """)
                rows = cursor.fetchall()
                if rows:
                    print(rows)
                    return True
                else:
                    print("pas de produits")
                    return False
            except:
                print("BUG")
        except:
            print("GROS BUG")

if My_substitutes():
    print("PRODUIT PRESENT ")
else:
    print("NOP")



