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

def main():
    with open('./data/clean_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())
    
    tagsDict = {}

    nReqs = 0

    for paper in papers:
        urlTags = paper["tags"]
        newTags = []
        
        for tag in urlTags:
            if tag not in tagsDict.keys():
                tagsDict[tag] = getTitle(tag)
                nReqs+=1
            
            newTags.append(tagsDict[tag])
        paper['tags'] = newTags

    file = open("./data/refined_data.json", "w+")
    json.dump(papers, file, indent=2)


if __name__ == '__main__':
    main()