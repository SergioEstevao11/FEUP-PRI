# PRI-project

## Metrics

precision, recall, average, mean average precision, precision recall curve

## To run Solr
cd src
docker build . -t papers
docker run -p 8983:8983 papers

## To run Server
cd src/server
npm i
npm run dev

## To run Website
cd src/scihub-light
npm i
npm start