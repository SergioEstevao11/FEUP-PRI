import json

def tags_oneident():
    #tags do gama
    with open('./data/refined_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())


    for paper in papers:

        tags = []

        for area in paper['tags']:
            for field in paper['tags'][area]:
                tag = {
                    "area": area,
                    "field": field,
                    "subjects": [],
                }

                for subject in paper['tags'][area][field]:
                    tag['subjects'].append(subject)
            tags.append(tag)

        paper['tagsNew'] = tags

        paper.pop('tags')


    file = open("./data/solr_data.json", "w+")
    json.dump(papers, file, indent=1)

def main():
    with open('./data/refined_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())


    for paper in papers:

        areas = []
        fields = []
        subjects = []

        for area in paper['tags']:
            areas.append(area)
            for field in paper['tags'][area]:
                fields.append(field)
                for subject in paper['tags'][area][field]:
                    subjects.append(subject)

        paper['areas'] = areas
        paper['fields'] = fields
        paper['subjects'] = subjects

        paper.pop('tags')


    file = open("./data/solr_data.json", "w+")
    json.dump(papers, file, indent=1)


if __name__ == '__main__':
    main()