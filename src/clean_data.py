import json
import ast

def contains_number(string):
    return any(char.isdigit() for char in string)


def main():
    with open('./data/arxivData.json', 'r') as dataset:
        papers = json.loads(dataset.read())
    for paper in papers:
        names = []

        # authors
        for author in ast.literal_eval(paper['author']):        
            names.append(author['name'])
        paper['authors'] = names

        # link
        for link in ast.literal_eval(paper['link']):
            if link['rel'] == 'alternate':
                paper['link'] = link['href']

        # date
        date = str(paper['year']) + '-' + str(paper['month']) + '-' +  str(paper['day']) 
        paper['date'] = date

        # tags
        tags = []
        for tag in ast.literal_eval(paper['tag']):
            if (contains_number(tag['term'])):
                continue
            tags.append(tag['term'])
        paper['tags'] = tags

        paper.pop('author')
        paper.pop('id')
        paper.pop('year')
        paper.pop('month')
        paper.pop('day')
        paper.pop('tag')


    file = open("./data/clean_data.json", "w+")
    json.dump(papers, file, indent=2)

if __name__ == '__main__':
    main()