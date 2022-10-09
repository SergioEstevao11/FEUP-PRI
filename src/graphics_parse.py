import matplotlib.pyplot as plt
import json
import numpy as np
import random

def piePlot(data, title, path):
    fig = plt.figure(figsize = (15, 10))

    explode = [0, 0.5] * 4

    print(data)
    pie = plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%',
    wedgeprops= {"edgecolor":"black",
                     'linewidth': 1,
                     'antialiased': True})
    hatches = ['o' if value==min(data) else 'O' if value==max(data) else '' for value in data]

    # for i in range(len(pie[0])):
    #     pie[0][i].set(hatch = hatches[i], fill=False)

    plt.title(title, fontsize=30)
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
    areaCounters["Others: \n-Quantitative Biology, \n-Electrical Engineering and Systems Science, \n-Quantitative Finance, \n-Economics"] = 0
    for paper in papers:

        for area in paper["tags"].keys():
            if area not in areaCounters.keys():
                areaCounters[area] = 1
            else:
                areaCounters[area] += 1

    

    for k in areaCounters.keys():
        if areaCounters[k] < 1000:
            areaCounters["Others: \n-Quantitative Biology, \n-Electrical Engineering and Systems Science, \n-Quantitative Finance, \n-Economics"] += areaCounters[k]
            
    del areaCounters["Quantitative Biology"]
    del areaCounters["Electrical Engineering and Systems Science"]
    del areaCounters["Quantitative Finance"]
    del areaCounters["Economics"]

    piePlot(areaCounters, "Most Common Areas", "../docs/res/areas.jpg")
    



def main():
    with open('./data/refined_data.json', 'r') as dataset:
        papers = json.loads(dataset.read())

    plotAreas(papers)

    # areaCounters = {}
    # #areaCounters["Others"] = 0
    # for paper in papers:

    #     for area in paper["tags"].keys():
    #         if area not in areaCounters.keys():
    #             areaCounters[area] = 1
    #         else:
    #             areaCounters[area] += 1

    # fig, ax = plt.subplots(figsize=(15, 10), subplot_kw=dict(aspect="equal"))

    # recipe = list(areaCounters.keys())

    # data = areaCounters.values()

    # zipped_lists = list(zip(recipe, data))

    # random.shuffle(zipped_lists)

    # tuples = zip(*zipped_lists)
    # recipe, data = [ list(tuple) for tuple in tuples]


    # wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    # bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    # kw = dict(arrowprops=dict(arrowstyle="-"),
    #         bbox=bbox_props, zorder=0, va="center")

    # for i, p in enumerate(wedges):
    #     ang = (p.theta2 - p.theta1)/2. + p.theta1
    #     y = np.sin(np.deg2rad(ang))
    #     x = np.cos(np.deg2rad(ang))
    #     horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    #     connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    #     kw["arrowprops"].update({"connectionstyle": connectionstyle})
    #     ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.6*y),
    #                 horizontalalignment=horizontalalignment, **kw)

    # ax.set_title("Matplotlib bakery: A donut")

    # plt.savefig("./plots/field.png")


if __name__ == '__main__':
    main()