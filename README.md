# Controle en cours
Une application "search-as-you-type" pour savoir quels sont les contrôles en cours, en AngularJS + Flask + Elasticsearch.


# Déploiement sur un serveur Ubuntu (testé sur 16.04)

## Préparation
Installer des paquets:
```
apt-get update
apt-get upgrade
apt-get install git python-pip curl screen
pip install --upgrade pip
```

## Installation depuis Github
Installer controle-en-cours depuis Github dans le dossier `deploy`:
```
mkdir ~/deploy && cd ~/deploy
git clone https://github.com/eig-2017/controle-en-cours
cd controle-en-cours
```

Créer un environnement virtuel sous Python 3 :
```
pip install virtualenv
virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Elasticsearch
Installer Java :
```
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
java -version
```

Installer Elasticsearch :
```
wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.6.deb
sudo dpkg -i elasticsearch-1.7.6.deb
```

Lancer Elasticsearch :
```
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch
```

## Prépartion des données et lancement du serveur
Indexer les données de `data/works.data` dans Elasticsearch :
```
make index
```

Lancer le backend :
```
make backend
```

Ouvrir une nouvelle fenêtre, par exemple avec `screen` (`Ctrl+a` puis `c`, voir [ici](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-screen-on-an-ubuntu-cloud-server)). Attention, dans la nouvelle fenêtre il faut réactiver l'environnement virtuel `source ./venv/bin/activate`.

Lancer le frontend :
```
make frontend
```

## Limites actuelles

- Quand la barre de recherche est vidée, les précédents résultats de recherche restent affichés.
- Pas de cache (chaque frappe lance une requête Elasticsearch).
- Pas de pagination.
- Version d'Elasticsearch obsolète.


# Note

Fork du projet [CheerMeApp](https://github.com/bonzanini/CheerMeApp-demo)
