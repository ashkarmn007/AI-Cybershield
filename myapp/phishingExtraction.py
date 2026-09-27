import numpy as np
from sklearn.ensemble import RandomForestClassifier as rfc
#from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as lr
from flask import jsonify

from myapp import feature_extraction


def getResult(url):
    # url="http://www.facebook.com"

    #Importing dataset
    # data = np.loadtxt( r"dataset.csv", delimiter = ",")
    data = np.loadtxt( r"D:\project\aicybershield\myapp\dataset.csv", delimiter = ",")
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!_____________________________________________________________________")

    # print(data)

    X = data[: , :-1]
    y = data[: , -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    clf = rfc()
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    # print(score*100)
    # print("hello")
    accuracy=str(score*100)

    X_new = []

    X_input = url
    ress=""
    # try:
    X_new=feature_extraction.generate_data_set(X_input)
    X_new = np.array(X_new).reshape(1,-1)

    # try:
    prediction = clf.predict(X_new)
    if prediction == -1:
        print('kas chascs')
        ress="Phishing Url"
        return ress,accuracy
    else:
        print('kahsbch')
        ress="Legitimate Url"
        return ress
    # except:
    #     print('akjsnckajssb')
    #     ress="Legitimate Url"
    #     return ress,accuracy
    # # except:
    #     ress="Phishing Url"
    #     return ress,accuracy

