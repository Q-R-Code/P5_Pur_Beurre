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
                cursor.execute("""SELECT * FROM substitutes_saved""")
                rows = cursor.fetchall()
                print(rows)
                print(rows[0])
                print(rows[0][1])
            except:
                print("BUG")
        except:
            print("GROS BUG")

My_substitutes()


