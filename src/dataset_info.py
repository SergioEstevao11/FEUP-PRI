import json

def main():
    with open('./data/solr_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())

    areas = set()
    fields = set()
    subjects = set()
    for paper in papers:
        for area in paper['areas']:
            areas.add(area)
        for field in paper['fields']:
            fields.add(field)
        for subject in paper['subjects']:
            subjects.add(subject)

        

    print("Unique areas: ", areas)
    print("\n\nUnique fields: ", fields)
    print("\n\nUnique subjects: ", subjects)


if __name__ == '__main__':
    main()