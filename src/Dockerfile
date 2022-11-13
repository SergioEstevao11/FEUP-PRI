FROM solr:8.10

COPY data/solr_data.json /data/solr_data.json

COPY solr/schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
