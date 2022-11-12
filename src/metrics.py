### SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import requests
import numpy as np
import pandas as pd

# BOOSTED = True
# QUERY_ID = "Milestone_2/queries/q5/q5"
# QUERY_URL =

def precision(result, relevants):
    return len(set(result) & set(relevants)) / len(result)

def recall(result, relevants):
    return len(set(result) & set(relevants)) / len(relevants)

def f1(result, relevants):
    prec = precision(result, relevants)
    rec = recall(result, relevants)
    return 2 * prec * rec / (prec + rec)

def plot_precision_recall_curve(precision, recall, average_precision, title):
    disp = PrecisionRecallDisplay(precision=precision, recall=recall)
    disp.plot(ax=plt.gca(), label="Precision-Recall curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(title)
    plt.legend(loc="best")
    plt.show()

def plot_precision_recall_curve_from_df(df, title):
    precision = df["precision"].to_numpy()
    recall = df["recall"].to_numpy()
    average_precision = df["average_precision"].to_numpy()
    plot_precision_recall_curve(precision, recall, average_precision, title)

def main():
    




if __name__ == "__main__":
    main()

