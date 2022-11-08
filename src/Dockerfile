FROM solr:8.10

COPY data/refined_data.json /data/refined_data.json

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
