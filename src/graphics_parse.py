import matplotlib.pyplot as plt
import json

def piePlot(data, title, path):
    fig = plt.figure(figsize = (15, 10))

    pie = plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    hatches = ['o' if value==min(data) else 'O' if value==max(data) else '' for value in data]

    for i in range(len(pie[0])):
        pie[0][i].set(hatch = hatches[i], fill=False)

    plt.title(title, fontsize=20)
    plt.axis('equal')
    plt.savefig(path)
    plt.show()

def barPlot(data, title, xAxis, yAxis, path):
    fig = plt.figure(figsize = (20, 10))

    plt.bar(data.keys(), data.values(), color ='maroon', width = 0.4)
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.title(title, fontsize=20)
    plt.savefig(path)
    plt.show()

def splitString(string):
    if '["' in string:
        allAuthors = string.split('["')
        allAuthors = allAuthors[1].split('"]')
        allAuthors = allAuthors[0].split('", "')
    else:
        allAuthors = string.split("['")
        allAuthors = allAuthors[1].split("']")
        allAuthors = allAuthors[0].split("', '")

    return allAuthors

def checkExistance(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

    
def plotAreas(papers):
    areaCounters = {}
    for paper in papers:

        for area in paper["tags"].keys():
            if area not in areaCounters.keys():
                areaCounters[area] = 1
            else:
                areaCounters[area] += 1

    piePlot(areaCounters, "Most Common Areas", "../docs/res/areas.jpg")
    



def main():
    with open('./data/refined_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())

    plotAreas(papers)


if __name__ == '__main__':
    main()