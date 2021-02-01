import requests
import mysql.connector

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

    cursor.execute("""SELECT * FROM category """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except mysql.connector.errors.InterfaceError as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
finally:
    connection.close()




