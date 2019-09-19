import matplotlib.pyplot as plt
import numpy as np
import time
import datetime as dt
from joblib import dump,load
from sklearn import datasets, svm, metrics
from sklearn.datasets import fetch_openml
from data_vis import *

def train():
    mnist = fetch_openml('MNIST_784', data_home='./')
    mnist.keys()
    images = mnist.data
    targets = mnist.target

    X_data = images / 255.0
    Y = targets

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X_data, Y,
                                                test_size=0.15,random_state=42)
    param_C = 100
    param_gamma = 0.1
    classifier = svm.SVC(C=param_C, gamma=param_gamma)
    start_time = dt.datetime.now()
    print('Start learning at {}'.format(str(start_time)))
    classifier.fit(X_train, y_train)
    dump(classifier,'model.joblib')
    end_time = dt.datetime.now()
    print('Stop learning {}'.format(str(end_time)))
    elapsed_time = end_time - start_time
    print('Elapsed learning {}'.format(str(elapsed_time)))

    expected = y_test
    predicted = classifier.predict(X_test)

    show_some_digits(X_test, predicted, title_text="Predicted {}")

    print("Classification report for classifier %s:\n%s\n"
          % (classifier, metrics.classification_report(expected, predicted)))

    cm = metrics.confusion_matrix(expected, predicted)
    print("Confusion matrix:\n%s" % cm)

    plot_confusion_matrix(cm)

    print("Accuracy={}".format(metrics.accuracy_score(expected, predicted)))

if __name__ == "__main__":
    train()
