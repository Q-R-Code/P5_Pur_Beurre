import mysql


class Sub_to_save():

    def __init__(self, product):
        self.name = None
        self.url = None
        self.image_url = None
        self.nutriscore_grade = None
        self.image_nutrition = None
        self.stores = None
        self.product = product
        self.split_data()
        self.save_in_db()

    def split_data(self):
        self.name = self.product.get('product_name')
        self.url = "https://fr.openfoodfacts.org/produit/{}".format(self.product.get("code"))
        self.image_url = self.product.get('image_url')
        self.nutriscore_grade = f"https://static.openfoodfacts.org/images/attributes/nutriscore-{self.product.get('nutriscore_grade')}.svg"
        self.image_nutrition = self.product.get('image_nutrition_url')
        self.stores = self.product.get('stores')

    def save_in_db(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                cursor.execute(f"""SELECT name FROM substitutes_saved WHERE name="{self.name}" """)
                rows = cursor.fetchall()
                if not rows:
                    cursor.execute(
                        f"""INSERT INTO substitutes_saved (name, url, image_url, nutrition_grade, image_nutrition, stores)
                        VALUES 
                        ("{self.name}", "{self.url}", "{self.image_url}", "{self.nutriscore_grade}","{self.image_nutrition}","{self.stores}")""")
                    connection.commit()
                else:
                    pass

            except:
                connection.rollback()

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            connection.close()


class Sub_to_delete():

    def __init__(self, product):
        self.product = product
        self.id = self.product[0]
        self.delete_to_db()

    def delete_to_db(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                cursor.execute(
                    f"""DELETE FROM `substitutes_saved` WHERE `substitutes_saved`.`Id` = {self.id} """)

                connection.commit()
            except:
                connection.rollback()

        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            connection.close()


class My_substitutes():

    def __init__(self):
        self.substitutes = []

    def get_substitues_saved(self):
        try:
            connection = mysql.connector.connect(host="localhost",
                                                 user="flynz",
                                                 password="openfoodfacts",
                                                 database="pur_beurre",
                                                 auth_plugin='mysql_native_password')
            cursor = connection.cursor()
            try:
                cursor.execute("""SELECT * FROM substitutes_saved""")
                products = cursor.fetchall()
            except:
                connection.rollback()
        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            connection.close()
        return products
