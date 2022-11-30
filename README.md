# PRI-project

## To test
query com boosts e sem boosts (piora, melhora ou não influencia)

com o nosso schema (um com varios filtros e outro sem) e sem schema e avaliar

## Metrics

precision, recall, average, mean average precision, precision recall curve

## To run Solr

docker build . -t papers
docker run -p 8983:8983 papers

## To run Django

cd src/search
> python -m venv .venv (para quem não tem venv ou prefere criar um novo)
> .venv\Scripts\Activate.ps1 ou .venv\Scripts\activate.bat                
(.venv) > python -m pip install django~=4.0.0
(.venv) > python manage.py migrate
(.venv) > python manage.py runserver

Criar admin

python manage.py createsuperuser