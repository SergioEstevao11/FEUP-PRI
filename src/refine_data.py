from csv import field_size_limit
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

def getMainAreaTitle(area):
    url = "https://arxiv.org/"

    response = requests.get(url)
    text = response.text

    mainIndex = text.find("<main>")
    areaIndex = text.find(area, mainIndex)

    #print("mainIndex: ", mainIndex)
    #print("areaIndex: ", areaIndex)

    #print("<<<<<<<<<<<<<<<", text[mainIndex:areaIndex])

    h2Index = text.rfind("<h2>", mainIndex, areaIndex)
    h2FinalIndex = text.rfind("</h2>", mainIndex, areaIndex)

    #print("h2Index: ", h2Index)
    #print("h2FinalIndex: ", h2FinalIndex)

    result = text[h2Index+4:h2FinalIndex]

    return result




def main():
    with open('./data/clean_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())
    
    tagsDict = {}
    areaDict = {}

    for paper in papers:
        urlTags = paper["tags"]
        newTags = {}
        
        for tag in urlTags:

            tokens = tag.split(".")
            field = tokens[0]
            if len(tokens) == 1: spec = tokens[0]
            else: spec = tokens[1]

            if field not in tagsDict.keys():
                tagsDict[field] = getTitle(field)

            if spec not in tagsDict.keys():
                tagsDict[spec] = getTitle(tag)

            if tag not in areaDict.keys():
                # if tagsDict[field] == "Computer Science":
                #     areaDict[spec] = "Computer Science"
                # else:
                #     areaDict[spec] = getMainAreaTitle(tagsDict[spec])
                areaDict[tag] = getMainAreaTitle(tag)


            

            areaTitle = areaDict[tag]
            fieldTitle = tagsDict[field]
            specTitle = tagsDict[spec]

            if areaTitle not in newTags.keys():
                newTags[areaTitle] = {}
            

            # print("areaTitle: ", areaTitle)
            # print("fieldTitle: ", fieldTitle)
            # print("specTitle: ", specTitle)
            # print(newTags)
            if fieldTitle not in newTags[areaTitle].keys():    
                newTags[areaTitle][fieldTitle] = [specTitle]
            else:
                newTags[areaTitle][fieldTitle].append(specTitle)

            # print(newTags)
            # print("================")
            
            
        paper['tags'] = newTags

    file = open("./data/refined_data.json", "w+")
    json.dump(papers, file, indent=2)


if __name__ == '__main__':
    main()