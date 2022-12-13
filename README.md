# PRI-FEUP
## Group: T05G05

| Name             | Number    |
| ---------------- | --------- |
| Beatriz Santos   | 201906888 |
| Sergio Estêvão   | 201905680 |
| Sergio da Gama   | 201906690 |


In this project, we developed a <b>search system</b> for <b>scientific articles</b>.

We started by analyzing the dataset and creating a pipeline to process and transform it. This resulted in the creation of a new data structure, which we visualized using a UML diagram. We then used Solr to retrieve information and tested it with different queries and boosts, as well as multiple schemas.

Finally, we developed an interactive web application using React, which allowed users to efficiently search through scientific articles in a customizable way.

## Solr
To run Solr, please input the following commands:
```
cd src
docker build . -t papers
docker run -p 8983:8983 papers
```

## To run Server (Backend)
To run the server, after running Solr's application, insert the following commands:
```
cd src/server
npm i
npm run dev
```

## User Interface (Frontend)
After the server is set, please input the next commands:
```
cd src/scihub-light
npm i
npm start
```

If Solr, Backend and Frontend are running, you can then join `https://localhost:3000/search` to interact with the user interface of our search system.

You can read the project's final report [here](docs/milestone3/report-55.pdf).

