# Queries

### 1.

A developer that is creating a ML model to predict cars longevity based on their velocity.

Query:
```
q: velocity
qf: link summary title authors date tagsNew.area tagsNew.field tagsNew.subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=velocity&q.op=OR&defType=edismax&indent=true&rows=50&qf=link%20summary%20title%20authors%20date%20tagsNew.area%20tagsNew.field%20tagsNew.subjects`

Boosted:
```
q: velocity
qf: link summary^10 title^2 authors date tagsNew.area tagsNew.field tagsNew.subjects
defType: edismax
```
`http://localhost:8983/solr/#/papers/query?q=velocity&q.op=OR&defType=edismax&indent=true&rows=50&qf=link%20summary%5E10%20title%5E2%20authors%20date%20tagsNew.area%20tagsNew.field%20tagsNew.subjects`
``
