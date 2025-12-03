# NoSQL - MongoDB

## Description
Ce projet est une introduction aux bases de données NoSQL, plus spécifiquement MongoDB. Tu vas apprendre à manipuler des documents, des collections et à effectuer des opérations CRUD (Create, Read, Update, Delete).

## Objectifs d'apprentissage
À la fin de ce projet, tu devrais être capable d'expliquer :

### Concepts généraux NoSQL
- Ce qu'est NoSQL
- La différence entre SQL et NoSQL
- Ce qu'est ACID
- Ce qu'est le stockage de documents
- Les types de bases de données NoSQL
- Les avantages d'une base de données NoSQL
- Comment requêter des informations depuis une base NoSQL
- Comment insérer/mettre à jour/supprimer des informations depuis une base NoSQL

### MongoDB
- Comment utiliser MongoDB
- Les commandes de base du shell MongoDB
- Comment utiliser pymongo pour interagir avec MongoDB depuis Python

## Ressources à consulter
- [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)
- [What is NoSQL?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [The mongo Shell](https://www.mongodb.com/docs/manual/mongo/)

## Prérequis
- MongoDB version 3.6 ou supérieur
- Python 3.7 ou supérieur
- pymongo
- Ubuntu 18.04 LTS

## Installation de MongoDB

```bash
# Import the public key used by the package management system
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

# Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Reload local package database
sudo apt-get update

# Install MongoDB
sudo apt-get install -y mongodb-org

# Start MongoDB
sudo service mongod start

# Verify installation
mongo --version
```

## Installation de pymongo

```bash
pip3 install pymongo
```

## Structure du projet

### Scripts MongoDB Shell
- `0-list_databases` : Liste toutes les bases de données
- `1-use_or_create_database` : Crée ou utilise une base de données
- `2-insert` : Insère un document dans une collection
- `3-all` : Liste tous les documents d'une collection
- `4-match` : Filtre les documents par critère
- `5-count` : Compte le nombre de documents
- `6-update` : Met à jour des documents
- `7-delete` : Supprime des documents

### Scripts Python
- `8-all.py` : Fonction pour lister tous les documents
- `9-insert_school.py` : Fonction pour insérer un document
- `10-update_topics.py` : Fonction pour mettre à jour les topics
- `11-schools_by_topic.py` : Fonction pour chercher par topic
- `12-log_stats.py` : Script d'analyse de logs Nginx

## Utilisation

### Scripts MongoDB Shell
Les scripts MongoDB peuvent être exécutés avec la commande `mongo` :

```bash
# Exemple pour lister les bases de données
cat 0-list_databases | mongo

# Exemple avec une base de données spécifique
cat 2-insert | mongo my_db
```

### Scripts Python
Les scripts Python doivent être exécutables :

```bash
chmod +x 8-all.py
./8-all.py
```

## Concepts clés à maîtriser

### Commandes MongoDB de base
- `show dbs` : Afficher les bases de données
- `use <db_name>` : Utiliser/créer une base de données
- `show collections` : Afficher les collections
- `db.collection.insert()` : Insérer un document
- `db.collection.find()` : Chercher des documents
- `db.collection.update()` : Mettre à jour des documents
- `db.collection.remove()` : Supprimer des documents
- `db.collection.count()` : Compter les documents

### Méthodes pymongo importantes
- `MongoClient()` : Se connecter à MongoDB
- `insert_one()` / `insert_many()` : Insérer des documents
- `find()` / `find_one()` : Chercher des documents
- `update_one()` / `update_many()` : Mettre à jour des documents
- `delete_one()` / `delete_many()` : Supprimer des documents
- `count_documents()` : Compter les documents

## Conseils pour réussir

1. **Commence par le shell MongoDB** : Maîtrise les commandes de base avant de passer à Python
2. **Teste chaque commande** : Utilise le shell interactif pour expérimenter
3. **Comprends la structure des documents** : Les documents MongoDB sont comme des dictionnaires Python
4. **Consulte la documentation** : La doc MongoDB est très bien faite
5. **Utilise les exemples** : Regarde les sorties attendues pour comprendre le comportement

## Auteur
Projet réalisé dans le cadre du cursus Holberton School

## License
Ce projet est sous licence éducative Holberton School
