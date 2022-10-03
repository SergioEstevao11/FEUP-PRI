import requests

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

def importCleanData(path):
    return 

def main():
    tagsDict = {}

    nReqs = 0

    for paper in papers:
        urlTags = paper['tags']
        newTags = []
        
        for tag in urlTags:
            if tag not in tagsDict.keys():
                tagsDict[tag] = getTitle(tag)
                nReqs+=1
            
            newTags.append(tagsDict[tag])
        paper['tags'] = newTags

    print("Number of requests made: ", nReqs)