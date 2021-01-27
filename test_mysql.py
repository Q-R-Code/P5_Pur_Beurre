import requests
import mysql.connector

req = requests.get("https://fr.openfoodfacts.org/categories.json")

try:
    connection = mysql.connector.connect(host="localhost",
                                         user="admin",
                                         password="openfoodfacts",
                                         database="openfoodfacts",
                                         auth_plugin='mysql_native_password')

    cursor = connection.cursor()

    try:
        # cursor.execute("""INSERT INTO category
        # VALUES (1, 'aliment1'), (2, 'aliment2'), (3, 'aliment3')""")

        connection.commit()

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




