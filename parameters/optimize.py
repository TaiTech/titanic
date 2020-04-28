import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from operator import itemgetter
import csv


# utility function to report top 5 optimal parameters
'''
def report(scores, n_top=5, verbose=True):
    params = None
    top_scores = sorted(scores, key=itemgetter(1), reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        if verbose is True:
            print("Parameters with rank: {0}".format(i + 1))
            print("Mean Test Score: {0:.4f} (std: {1:.4f})".format(
                score.mean_test_score,
                np.std(score.cv_validation_scores)))
            print("Parameters: {0}".format(score.params))
            print("")
        if params is None:
            params = score.params
    return params
'''


# function to optimize hyperparameters need for the random forest classifier
def optimize_hyperparameters(df):
    n_samples = df.shape[0]
    random_test = {
        'n_estimators' : np.linspace(n_samples * 2, n_samples * 10, 5).astype(int),
        'criterion': ['gini', 'entropy'],
        'max_features': [None, 'sqrt', 'log2'],
        'min_samples_split': np.linspace(2, n_samples / 50, 10).astype(int),
        'min_samples_leaf': np.linspace(1, n_samples / 200, 10).astype(int),
        'max_leaf_nodes': np.linspace(10, n_samples / 50, 10).astype(int)
    }
    clf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)
    values_ = df.values[:, :-1]
    X = values_
    y = df.values[:, -1]

    random_search = RandomizedSearchCV(clf, random_test, n_jobs=-1, cv=10,
                                       n_iter=2, random_state=42)

    print("Fit...")
    random_search.fit(X, y)
    # print("Report...")
    # best_params = report(random_search.cv_results_, verbose=False)
    best_params = random_search.best_params_
    # save best hyperparameters to csv
    with open('./temp/best_params.csv', 'wt') as f:
        w = csv.DictWriter(f, best_params.keys())
        w.writeheader()
        w.writerow(best_params)
