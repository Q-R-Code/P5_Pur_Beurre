# Utilisez les données publiques de l'OpenFoodFacts #

Cet outil aidera les utilisateurs de la start-up Pur Beurre afin de comparer et de leur proposer des produits
alimentaire plus sains. Pour cela, nous faisons appel à l'API de OpenFoodFacts.

Une interface graphique sera proposée graçe à Flask, vous aurez alors la possibilité de rechercher un produit par son
code barre ( EAN ). Une selection de categories et produits populaires sera présent sur la page d'acceuil.

Lors de votre visite, vous aurez la possibilité d'enregistrer un substitut afin de le retrouver dans "Mes produits".

-------------------------------------------------------------------------------

## Instalation & lancement ##

Télécharger et décompresser le repository puis créer un VENV. Installez ensuite le requirements.txt

    pip3 install -r requirements.txt

Lors du premier lancement de l'application, vous devez initialiser les tables de la base de donnée:

    python3 main.py init

Ensuite, vous pouvez simplement démarrer l'application avec :

    python3 main.py run

----------------------------------------------------------------------------

## Fonctionnement ##

- ### Accueil :
  Une barre de recherche permettant de retrouver un produit par rapport à son code barre EAN et un request API
  Openfoodfacts. Retourne une page avec le produit recherché. Deux sections sont aussi présentes. La premiere "les
  catégories populaires" sur OpenFoodFacts et ensuite une selection de produits populaires. Ces deux sections sont
  affichées depuis la base de données au préalablement chargé grace à un appel API.


- ### Produit recherché :
  Affiche les caractéristiques (Nom, URL, Nutriscore, Valeurs nutritionnelles) et jusqu'à 5 substituts, avec un
  nutriscore intéressant et des catégories similaires, sont proposés. Il est possible qu'il n'y est pas de substitut
  plus sain pour votre recherche. Pour chaques substituts trouvés, vous avez alors la possibilité de le sauvegarder afin
  de le retrouver dans "Menu>Mes produits". Attention relancer l'application avec l'option "init" réinitialisera
  totalement la base de données!

- ### Mes produits :
  Vous retrouvez vos produits mis de cotés. Une touche est présente pour retirer ce produit.

---------------------------------------------------------------------------------------

## Modules :

- main.py : Permet l'initialisation du programme.
- create_db.py : Les différentes tables nécessaires au fonctionnement.
- cat_products_popular.py : Ce module request les catégories et des produits populaires sur l'API de OpenFoodFacts.
  Charge ensuite les données dans les tables prévues à cet effet.
- search_product.py : Est appelé lors du lancement d'une recherche. Récupération du code barre pour faire une request
  API. Il Récupère ensuite les données du produit et des substituts pour retourner la route "/products"
  contenant les informations et la possibilité d'enregistrer un substitut.
- substitute_in_db.py : Récupère dans la table "substitutes_saved" les produits présent. Un affichage est proposé, un
  bouton permet de retirer un produit enregistré. 
  
---------------------------------------------------------------------------------------

### Version : 

- 1.0 : Premiere version stable et fonctionnelle du programme.
  

 






