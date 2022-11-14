# Queries

### 1.

A developer that is creating a ML model to predict cars longevity based on their velocity.

Query:
```
q: velocity
qf: link summary title authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=velocity&q.op=OR&defType=edismax&indent=true&rows=100&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects`

Boosted:
```
q: velocity
qf: link summary^10 title^2 authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=velocity&q.op=OR&defType=edismax&indent=true&rows=50&qf=link%20summary%5E10%20title%5E2%20authors%20date%20areas%20fields%20subjects`
``


### 2.

A Data analyst that is processing a dataset and needs to understand normal distributions.

Query:
```
q: normal distribution
qf: link summary title authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=normal%20distribution&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50`

Boosted:
```
q: normal distribution
qf: link summary^2 title^10 authors date areas fields subjects
bq: areas:Statistics^10
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=normal%20distribution&q.op=AND&defType=dismax&indent=true&qf=link%20summary%5E2%20title%5E10%20authors%20date%20areas%20fields%20subjects&rows=50&bq=areas:Statistics%5E20`
``

### 3.

A Writer wants to writer a biography about Francis Bach, but wants to focus on his algorithmic work from 2008 to 2018 mostly, but not exclusevly, from the year of 2015.

Query:
```
q: Francis Bach algorithm
qf: link summary title authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=Francis%20Bach%20algorithm&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50&fq=date:%5B2008-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`

Boosted:
```
q: Francis Bach algorithm
qf: link summary^5 title authors^5 date areas fields subjects
bf: if(and(gte(ms(date),ms(2015-01-01T00:00:00Z)),lt(ms(date),ms(2016-01-01T00:00:00Z))),10,0.1)
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=Francis%20Bach%20algorithm&q.op=AND&defType=dismax&indent=true&qf=link%20summary%5E5%20title%20authors%5E10%20date%20areas%20fields%20subjects&rows=50&bf=if(and(gte(ms(date),ms(2015-01-01T00:00:00Z)),lt(ms(date),ms(2016-01-01T00:00:00Z))),10,0.1)&fq=date:%5B2008-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`
``

### 4.

A researcher in the area of Statistics wants to try some new approaches related to his case study in linguistics.

Query:
```
q: areas:(statistics) new approaches linguistics
qf: link summary title authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=areas:(statistics)%20new%20approaches%20linguistics&q.op=AND&defType=edismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50`

Boosted:
```
q: new approaches
qf: link summary title^2 authors date areas fields subjects
pf: title^10
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=areas:(statistics)%20new%20approaches%20linguistics&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%5E2%20authors%20date%20areas%20fields%20subjects&rows=50&pf=title%5E10`
``

### 5.

A student that wants to get all the papers of related economics and computer science, in the year of 2017.

Query:
```
q: subjects:(Artificial Intelligence) economics
fq: date:[2017-01-01T00:00:00Z TO 2018-01-01T00:00:00Z}
qf: link summary title authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=Computer%20Science%20economics&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50&fq=date:%5B2017-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`

Boosted:
```
q: subjects:(Artificial Intelligence) economics
fq: date:[2017-01-01T00:00:00Z TO 2018-01-01T00:00:00Z}
qf: link summary title authors date areas^5 fields^5 subjects^5
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=computer%20science%20economics&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%5E5%20fields%5E5%20subjects%5E5&rows=50&fq=date:%5B2017-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`
``