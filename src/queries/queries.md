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

A Writer wants to writer a biography about Francis Bach, but wants to focus on his algorithmic work in the years 2014 until 2017, specially, in the year of 2015.

Query:
```
q: authors:(Francis Bach) algorithm
fq: date:[2014-01-01T00:00:00Z TO 2018-01-01T00:00:00Z}
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=authors:(Francis%20Bach)%20algorithm&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50&fq=date:%5B2014-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`

Boosted:
```
q: authors:(Francis Bach) algorithm
fq: date:[2014-01-01T00:00:00Z TO 2018-01-01T00:00:00Z}
bf: if(and(gte(ms(date),ms(2015-01-01T00:00:00Z)),lt(ms(date),ms(2016-01-01T00:00:00Z))),10,0.1)
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=authors:(Francis%20Bach)%20algorithm&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50&bf=if(and(gte(ms(date),ms(2015-01-01T00:00:00Z)),lt(ms(date),ms(2016-01-01T00:00:00Z))),10,0.1)&fq=date:%5B2014-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`
``

### 4.

A researcher that wants to try some new approaches on their work.

Query:
```
q: new approaches
qf: link summary title authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=new%20approaches&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50`

Boosted:
```
q: new approaches
qf: link summary title^2 authors date areas fields subjects
pf: title^10
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=new%20approaches&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%5E2%20authors%20date%20areas%20fields%20subjects&rows=50&pf=title%5E10`
``

### 5.

A student that wants to get all the papers related economics and to the Artificial Intelligence subject, in the year of 2017.

Query:
```
q: subjects:(Artificial Intelligence) economics
fq: date:[2017-01-01T00:00:00Z TO 2018-01-01T00:00:00Z}
qf: link summary title authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=subjects:(Artificial%20Intelligence)%20economics&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50&fq=date:%5B2017-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`

Boosted:
```
q: subjects:(Artificial Intelligence) economics
fq: date:[2017-01-01T00:00:00Z TO 2018-01-01T00:00:00Z}
qf: link summary title^10 authors date areas fields subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=subjects:(Artificial%20Intelligence)%20economics&q.op=AND&defType=dismax&indent=true&qf=link%20summary%20title%5E10%20authors%20date%20areas%20fields%20subjects&rows=50&fq=date:%5B2017-01-01T00:00:00Z%20TO%202018-01-01T00:00:00Z%7D`
``

### example.

A Student who wants to learn about black holes

Query:
```
q: black holes
qf: link summary title authors date area field subjects
defType: edismax
```

`http://localhost:8983/solr/papers/select?defType=edismax&indent=true&q.op=OR&q=black%20hole&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=100`