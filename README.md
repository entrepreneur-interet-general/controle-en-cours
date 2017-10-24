# Controle en cours

Une application "search-as-you-type" pour savoir quels sont les contrôles en cours, en AngularJS + Flask + Elasticsearch.



# Installation

Assumptions:

- Elasticsearch is running locally (localhost:9200)
- Tested on Elasticsearch 1.* (the mapping doesn't work on Elasticsearch 2.* )
- Tested on Python 3.4
- Use virtualenv to install Python dependencies

Clone repo, install virtualenv, install Python dependencies:
```
git clone https://github.com/bonzanini/controle-en-cours-demo
cd controle-en-cours-demo
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Create basic database (use data from `data/works.data`)::
```
make index
```

Run backend service::
```
make backend
```

Run frontend service::
```
make frontend
```

Point your browser to::
```
http://localhost:8000
```

and search for a controle.


# Limitation

- When the search bar is emptied, previous results are not cleared
  until a new search is issued.
- No caching (each keystroke is an Elasticsearch query) yet.
- No pagination yet.
- Elasticsearch 2.* is not yet supported


# Note

Fork du projet [CheerMeApp](https://github.com/bonzanini/CheerMeApp-demo)
