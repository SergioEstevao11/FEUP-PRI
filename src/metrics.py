### SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import requests
import numpy as np
import pandas as pd

#data for query evalution
BOOSTED = False
QUERY_ID = "q2"
QUERY_URL = "http://localhost:8983/solr/papers/select?defType=edismax&indent=true&q.op=OR&q=black%20hole&qf=link%20summary%20title%20authors%20date%20areas%20fields%20subjects&rows=100"

def precision(result, relevants, n=10):
    return len(set(result[:n]) & set(relevants)) / n

def recall(result, relevants):
    return len(set(result) & set(relevants)) / len(relevants)

def f1(result, relevants):
    prec = precision(result, relevants)
    rec = recall(result, relevants)
    return 2 * prec * rec / (prec + rec)

def plot_precision_recall_curve(precision, recall, title):
    disp = PrecisionRecallDisplay(precision=precision, recall=recall)
    disp.plot(ax=plt.gca(), label="Precision-Recall curve")
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
    plot_precision_recall_curve(precision, recall, average_precision, title)

def schema_evalution():
    #MEAN AVERAGE PRECISION
    #MEAN AVERAGE RECALL
    #MEAN AVERAGE F1
    queries = list(map(lambda el: el.rstrip(), open("queries/allqueries.txt").readlines()))
    relevants = [ list(map(lambda el: el.rstrip(), open("./queries/q" + str(id) + "/relevants.txt").readlines())) for id in range(1, len(queries)+1)]
    results = list(map(lambda url: requests.get(url).json()['response']['docs'], queries))
    for i in range(len(results)):
        results[i] = list(map(lambda x: x['id'], results[i]))

    precisions = [precision(results[i], relevants[i]) for i in range(len(results))]
    recalls = [recall(results[i], relevants[i]) for i in range(len(results))]
    f1s = [f1(results[i], relevants[i]) for i in range(len(results))]
    print("average precision: ", sum(precisions) / len(precisions))
    print("average recall: ", sum(recalls) / len(recalls))
    print("average f1: ", sum(f1s) / len(f1s))


    X_axis = np.arange(len(queries))

    plt.bar(X_axis - 0.2, precisions, 0.4, label = 'Precision')
    plt.bar(X_axis + 0.2, recalls, 0.4, label = 'Recall')
    
    plt.xticks(X_axis, map(lambda x: "q" + str(x), range(len(queries))))
    plt.xlabel("Queries")
    plt.title("Precision and Recall for each query")
    plt.legend()
    plt.savefig("./queries/allqueries.pdf")

    precision_recall_match = []
    for j in range(len(queries)):
        precision_values = [precision(results[j], relevants[j][:i]) for i in range(1, len(relevants) + 1)]
        recall_values = [recall(results[j], relevants[j][:i]) for i in range(1, len(relevants) + 1)]
        precision_recall_match.append( {k: v for k,v in zip(recall_values, precision_values)})
        print("og_recall: ", recall_values)

        # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
        recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
        recall_values = sorted(set(recall_values))

        # Extend matching dict to include these new intermediate steps
        for idx, step in enumerate(recall_values):
            if step not in precision_recall_match[j]:
                if recall_values[idx-1] in precision_recall_match[j]:
                    precision_recall_match[j][step] = precision_recall_match[j][recall_values[idx-1]]
                else:
                    precision_recall_match[j][step] = precision_recall_match[j][recall_values[idx+1]]
        

    frst = precision_recall_match[0]
    df = pd.DataFrame.from_dict(frst, orient='index')
    df.columns = ["precision"]
    df["recall"] = df.index
    print("df: \n", df)
    ax = \
    df.plot.line(x='recall', y='precision', markersize=3, style='-o', label="Q1", figsize=(9, 6))

    for idx in range(1, len(precision_recall_match)):
        df = pd.DataFrame.from_dict(precision_recall_match[idx], orient='index')
        df.columns = ["precision"]
        df["recall"] = df.index
        df.plot.line(x='recall', y='precision', markersize=3, style='-o', label="Q"+str(idx+1), ax=ax)


    plt.title("Recall-precision graphs")
    plt.xlabel("Recall (R@n)")
    plt.ylabel("Precision (P@n)")
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.grid()
    plt.legend(loc="lower right", ncol=7)
    plt.savefig('./queries/all-recall-precision.pdf', bbox_inches='tight')

def query_evalution():
    result = requests.get(QUERY_URL).json()['response']['docs']
    result = list(map(lambda x: x['id'], result))
    relevants = list(map(lambda el: el.rstrip(), open("./queries/" + QUERY_ID + "/relevants.txt").readlines()))
    
    precision_values = [precision(result, relevants[:i]) for i in range(1, len(relevants) + 1)]
    recall_values = [recall(result, relevants[:i]) for i in range(1, len(relevants) + 1)]
    f1_values = [f1(result, relevants[:i]) for i in range(1, len(relevants) + 1)]

    precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

    print("og_recall: ", recall_values)

    # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
    recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
    recall_values = sorted(set(recall_values))

    # Extend matching dict to include these new intermediate steps
    for idx, step in enumerate(recall_values):
        if step not in precision_recall_match:
            if recall_values[idx-1] in precision_recall_match:
                precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
            else:
                precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]
    
    print("precision_recall_match", precision_recall_match)

    print("precision values: ", precision_values)
    print("recall values: ", recall_values)
    print("f1 values: ", f1_values)

    plot_precision_recall_curve([precision_recall_match.get(r) for r in recall_values], recall_values, title="Precision-Recall curve")


def main():
    schema_evalution()
    #query_evalution()



if __name__ == "__main__":
    main()

