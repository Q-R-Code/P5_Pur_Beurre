# Utilisez les données publiques de l'OpenFoodFacts #


Cet outil aidera les utilisateurs de la start-up Pur Beurre afin de comparer et de leur proposer des produits alimentaire
plus sains. 
Pour cela, nous faisons appel à l'API de OpenFoodFacts.

Une interface graphique sera proposée graçe à Flask, vous aurez alors la possibilité de rechercher un produit par son code barre ( EAN ).
Une selection de categories et produits populaires sera présent sur la page d'acceuil.

Lors de votre visite, vous aurez la possibilité d'enregistrer un substitut afin de le retrouver dans "Mes produits".

-------------------------------------------------------------------------------

## Instalation & lancement ##

Télécharger et décompresser le repository puis créer un VENV. Installez ensuite le requirements.txt

    pip3 install -r requirements.txt

Lors du premier lancement de l'application, vous devez initialiser les tables de la base de donnée:

    python3 main.py -ma_commande

Ensuite, vous pouvez simplement démarrer l'application avec :

    python3 main.py

Si vous souhaitez mettre à jours les catégories et produits populaires de l'écran d'acceuil:

    python3 main.py -mon_autre_commande

----------------------------------------------------------------------------

## Fonctionnement ##







