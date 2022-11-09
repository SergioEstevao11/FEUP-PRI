# PRI-project

## To test
query com boosts e sem boosts (piora, melhora ou não influencia)

com o nosso schema (um com varios filtros e outro sem) e sem schema e avaliar

## Metrics

precision, recall, average, mean average precision, precision recall curve

## To run Solr

docker build . -t papers
docker run -p 8983:8983 papers