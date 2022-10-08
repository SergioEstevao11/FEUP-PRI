import requests
import json

def getTitle(tag):
    URL = 'https://arxiv.org/list/'
    url = URL + tag + '/recent'

    response = requests.get(url)
    text = response.text

    dlPageIndex = text.find("dlpage")

    h1Index = text.find("<h1>", dlPageIndex+1)
    h1FinalIndex = text.find("</h1>", h1Index)

    result = text[h1Index+4:h1FinalIndex-1]
    return result

def getAreaTitle(tag):
    pass


def main():
    with open('./data/clean_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())
    
    tagsDict = {}

    for paper in papers:
        urlTags = paper["tags"]
        newTags = {}
        
        for tag in urlTags:

            tokens = tag.split(".")
            area = tokens[0]
            if len(tokens) == 1: field = tokens[0]
            else: field = tokens[1]

            if area not in tagsDict.keys():
                tagsDict[area] = getTitle(area)

            if field not in tagsDict.keys():
                tagsDict[field] = getTitle(tag)

            areaTitle = tagsDict[area]
            fieldTitle = tagsDict[field]

            if areaTitle not in newTags.keys():
                newTags[areaTitle] = [fieldTitle]
            else:
                newTags[areaTitle].append(fieldTitle)
            
            
        paper['tags'] = newTags

    file = open("./data/refined_data.json", "w+")
    json.dump(papers, file, indent=2)


if __name__ == '__main__':
    main()