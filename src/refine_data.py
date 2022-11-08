from csv import field_size_limit
import requests
import json

def getUpdatedTag(tag):
    URL = 'https://arxiv.org/list/'
    url = URL + tag + '/recent'

    response = requests.get(url)
    text = response.text

    headerIndex = text.find("header")
    dlPageIndex = text.find("dlpage")

    updatedTagIndex = text.rfind("/list/", headerIndex, dlPageIndex)
    updatedTagIndexFinal = text.rfind("/recent", headerIndex, dlPageIndex)

    result = text[updatedTagIndex+6:updatedTagIndexFinal]

    return result



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

def getMainAreaTitle(area):
    url = "https://arxiv.org/"

    response = requests.get(url)
    text = response.text

    mainIndex = text.find("<main>")
    areaIndex = text.rfind(area, mainIndex)

    h2Index = text.rfind("<h2>", mainIndex, areaIndex)
    h2FinalIndex = text.rfind("</h2>", mainIndex, areaIndex)

    result = text[h2Index+4:h2FinalIndex]

    return result




def main():
    with open('./data/clean_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())

    updatedTags = {}
    tagsDict = {}
    areaDict = {}

    for paper in papers:

        urlTags = paper["tags"]
        newTags = {}

        for tag in urlTags:

            if tag not in updatedTags.keys():
                updatedTags[tag] = getUpdatedTag(tag)
            tag = updatedTags[tag]

            tokens = tag.split(".")
            field = tokens[0]
            if len(tokens) == 1: spec = tokens[0]
            else: spec = tokens[1]

            if field not in tagsDict.keys():
                tagsDict[field] = getTitle(field)

            if spec not in tagsDict.keys():
                tagsDict[spec] = getTitle(tag)

            if ("pastweek" in tagsDict[field]) or ("pastweek" in tagsDict[spec]):
                continue

            if tag not in areaDict.keys():
                areaDict[tag] = getMainAreaTitle(tag)


            areaTitle = areaDict[tag]
            fieldTitle = tagsDict[field]
            specTitle = tagsDict[spec]

            if areaTitle not in newTags.keys():
                newTags[areaTitle] = {}


            if fieldTitle not in newTags[areaTitle].keys():
                newTags[areaTitle][fieldTitle] = [specTitle]
            elif specTitle not in newTags[areaTitle][fieldTitle]:
                newTags[areaTitle][fieldTitle].append(specTitle)




        paper['tags'] = newTags

    file = open("./data/refined_data.json", "w+")
    json.dump(papers, file, indent=2)


if __name__ == '__main__':
    main()