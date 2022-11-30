### SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import requests
import numpy as np
import pandas as pd

#data for query evalution
BOOSTED = True
QUERY_ID = "q4"
QUERY_URL = "http://localhost:8983/solr/papers/select?defType=edismax&indent=true&q.op=AND&q=areas%3A(statistics)%20new%20approaches%20linguistics&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=50"

def precision(result, relevants, n=10):
    return len(set(result[:n]) & set(relevants)) / n

def recall(result, relevants, n=10):
    return len(set(result[:n]) & set(relevants)) / len(relevants)

def f1(result, relevants):
    prec = precision(result, relevants)
    rec = recall(result, relevants)
    return 2 * prec * rec / (prec + rec)

def plot_precision_recall_curve(precision, recall, title):
    disp = PrecisionRecallDisplay(precision=precision, recall=recall)
    disp.plot(ax=None, label="Precision-Recall curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(title)
    plt.legend(loc="best")
    boosted_text = "boosted" if BOOSTED else ""
    plt.savefig("./queries/" + QUERY_ID + "/" + boosted_text + 'results.pdf')


def plot_precision_recall_curve_from_df(df, title):
    precision = df["precision"].to_numpy()
    recall = df["recall"].to_numpy()
    average_precision = df["average_precision"].to_numpy()
    plot_precision_recall_curve(precision, recall, title)

def schema_evalution():
    #MEAN AVERAGE PRECISION
    #MEAN AVERAGE RECALL
    #MEAN AVERAGE F1
    boosted_text = "boosted" if BOOSTED else ""

    queries = list(map(lambda el: el.rstrip(), open("./queries/allqueries" + boosted_text + ".txt").readlines()))
    relevants = [ list(map(lambda el: el.rstrip(), open("./queries/q" + str(id) + "/relevants.txt").readlines())) for id in range(1, len(queries)+1)]
    results = list(map(lambda url: requests.get(url).json()['response']['docs'], queries))
    for i in range(len(results)):
        results[i] = list(map(lambda x: x['id'], results[i]))

    precisions = [precision(results[i], relevants[i]) for i in range(len(results))]
    recalls = [recall(results[i], relevants[i], len(results[i])+1) for i in range(len(results))]
    print("precisions: ", precisions)
    print("recalls: ", recalls)
    # f1s = [f1(results[i], relevants[i]) for i in range(len(results))]
    print("average precision: ", sum(precisions) / len(precisions))
    print("average recall: ", sum(recalls) / len(recalls))
    # print("average f1: ", sum(f1s) / len(f1s))


    X_axis = np.arange(len(queries))




    plt.bar(X_axis - 0.2, precisions, 0.4, label = 'Precision@10')
    plt.bar(X_axis + 0.2, recalls, 0.4, label = 'Recall')
    
    plt.xticks(X_axis, map(lambda x: "q" + str(x+1), range(len(queries))))
    plt.xlabel("Queries")
    plt.title("Precision and Recall for each query")
    plt.legend()
    plt.savefig("./queries/allqueries" + boosted_text + ".pdf")

    precision_recall_match = []
    for j in range(len(queries)):
        # precision_values = [precision(results[j], relevants[j], i) for i in range(1, len(results[j]) + 1)]
        # recall_values = [recall(results[j], relevants[j], i) for i in range(1, len(results[j]) + 1)]
        precision_values = [precision(results[j], relevants[j], i) for i in range(1, 51)]

        #interpolate
        i = len(precision_values)-2
        while i>=0:
            if precision_values[i+1]>precision_values[i]:
                precision_values[i]=precision_values[i+1]
            i=i-1

        recall_values = [recall(results[j], relevants[j], i) for i in range(1, 51)]
        precision_recall_match.append( {k: v for k,v in zip(recall_values, precision_values)})
        # print("og_recall: ", recall_values)
        # print("og_precision: ", precision_values)

        # #Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
        # recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
        # recall_values = sorted(set(recall_values))

        # # Extend matching dict to include these new intermediate steps
        # for idx, step in enumerate(recall_values):
        #     if step not in precision_recall_match[j]:
        #         if recall_values[idx-1] in precision_recall_match[j]:
        #             precision_recall_match[j][step] = precision_recall_match[j][recall_values[idx-1]]
        #         else:
        #             precision_recall_match[j][step] = precision_recall_match[j][recall_values[idx+1]]
        

    frst = precision_recall_match[0]
    df = pd.DataFrame.from_dict(frst, orient='index')
    df.columns = ["precision"]
    df["recall"] = df.index
    ax = \
    df.plot.line(x='recall', y='precision', markersize=3, style='-o', label="Q1", figsize=(9, 6))
    styles = ['-v', '-s', '-^', '-<', '-p', '-*', '-h', '-H', '-+', '-x', '-D', '-d', '-|', '-_', '-.']
    for idx in range(1, len(precision_recall_match)):
        df = pd.DataFrame.from_dict(precision_recall_match[idx], orient='index')
        df.columns = ["precision"]
        df["recall"] = df.index
        df.plot.line(x='recall', y='precision', markersize=3, style=styles[idx], label="Q"+str(idx+1), ax=ax)


    plt.title("Precision-recall graphs")
    plt.xlabel("Recall (R@n)")
    plt.ylabel("Precision (P@n)")
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.grid()
    plt.legend(loc="lower right", ncol=7)
    plt.savefig('./queries/all-precision-recall' + boosted_text +'.pdf', bbox_inches='tight')



def query_evalution():
    result = requests.get(QUERY_URL).json()['response']['docs']
    result = list(map(lambda x: x['id'], result))
    relevants = list(map(lambda el: el.rstrip(), open("./queries/" + QUERY_ID + "/relevants.txt").readlines()))
    
    precision_values = [precision(result, relevants, i) for i in range(1, 51)]
    recall_values = [recall(result, relevants, i) for i in range(1, 51)]
    # f1_values = [f1(result, relevants[:i]) for i in range(1, len(relevants) + 1)]

    precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

    print("og_recall: ", recall_values)

    # # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
    # recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
    # recall_values = sorted(set(recall_values))

    # # Extend matching dict to include these new intermediate steps
    # for idx, step in enumerate(recall_values):
    #     if step not in precision_recall_match:
    #         if recall_values[idx-1] in precision_recall_match:
    #             precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
    #         else:
    #             precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]
    
    print("precision_recall_match", precision_recall_match)

    print("precision values: ", precision_values)
    print("recall values: ", recall_values)
    
    precisions_for_plot = [precision_recall_match.get(r) for r in recall_values]

    #interpolation
    i = len(precisions_for_plot)-2
    while i>=0:
        if precisions_for_plot[i+1]>precisions_for_plot[i]:
            precisions_for_plot[i]=precisions_for_plot[i+1]
        i=i-1

    plot_precision_recall_curve(precisions_for_plot, recall_values, title="Precision-Recall curve")


def main():
    schema_evalution()
    #query_evalution()

    #simple query evaluation
    # result = requests.get(QUERY_URL).json()['response']['docs']
    # result = list(map(lambda x: x['id'], result))
    # relevants = list(map(lambda el: el.rstrip(), open("./queries/" + QUERY_ID + "/relevants.txt").readlines()))

    # p = precision(result, relevants)
    # r = recall(result, relevants)
    # f = f1(result, relevants)

    # print("precision: ", p)
    # print("recall: ", r)
    # print("f1: ", f)



if __name__ == "__main__":
    main()

