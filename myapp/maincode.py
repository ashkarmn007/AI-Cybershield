

from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline
from matplotlib import pyplot
from numpy import where
from sklearn.metrics import confusion_matrix

import numpy as np





#
# # define dataset
# X, y = make_classification(n_samples=10000, n_features=8, n_redundant=0,
# 	n_clusters_per_class=1, weights=[0.99], flip_y=0, random_state=1)
#
# print(type(X),type(y))
# print(X[0])
# # summarize class distribution
# counter = Counter(y)
# print(counter)
# # define pipeline
# over = SMOTE(sampling_strategy=0.1)
# under = RandomUnderSampler(sampling_strategy=0.5)
# steps = [('o', over), ('u', under)]
# pipeline = Pipeline(steps=steps)
# # transform the dataset
# X, y = pipeline.fit_resample(X, y)
# # summarize the new class distribution
# counter = Counter(y)
# print(counter)
# # scatter plot of examples by class label
# for label, _ in counter.items():
# 	row_ix = where(y == label)[0]
# 	pyplot.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))
# pyplot.legend()
# pyplot.show()


# Oversample and plot imbalanced dataset with SMOTE
from collections import Counter
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
from matplotlib import pyplot
from numpy import where
# define dataset
# X, y = make_classification(n_samples=10000, n_features=2, n_redundant=0,
# 	n_clusters_per_class=1, weights=[0.99], flip_y=0, random_state=1)

# summarize class distribution


X=[]
y=[]

def traing():
    training_data = np.loadtxt(r"C:\Users\Shamna PP\PycharmProjects\aicybershield\myapp\dataset.txt", dtype=str, delimiter=",")
    for record in training_data:
        print(record)

        if record[0] != '':
            lis = []
            lis.append(int(record[0].replace('A','')))
            lis.append(int(record[1].replace('A','')))
            lis.append(int(record[2].replace('A','')))
            lis.append(int(record[3].replace('A','')))
            lis.append(int(record[4].replace('A','')))
            lis.append(int(record[5].replace('A','')))
            lis.append(int(record[6].replace('A','')))
            lis.append(int(record[7].replace('A','')))
            lis.append(int(record[8].replace('A','')))
            lis.append(int(record[9].replace('A','')))
            lis.append(int(record[10].replace('A','')))
            lis.append(int(record[11].replace('A','')))
            lis.append(int(record[12].replace('A','')))
            lis.append(int(record[13].replace('A','')))
            lis.append(int(record[14].replace('A','')))
            lis.append(int(record[15].replace('A','')))
            lis.append(int(record[16].replace('A','')))
            lis.append(int(record[17].replace('A','')))
            lis.append(int(record[18].replace('A','')))
            lis.append(int(record[19].replace('A','')))


            X.append(lis)
            y.append(record[20])
            # self.training_set[record[13]].append(lis)

traing()

X=np.array(X)
y=np.array(y)
print(len(X),"X-Length")

counter = Counter(y)
print(counter)
# transform the dataset
oversample = SMOTE()
X, y = oversample.fit_resample(X, y)
print(X[0],y[0])
# summarize the new class distribution
counter = Counter(y)
print(counter)
# scatter plot of examples by class label
# for label, _ in counter.items():
# 	row_ix = where(y == label)[0]
# 	pyplot.scatter(X[row_ix, 0], X[row_ix, 1], label=str(label))
# pyplot.legend()
# pyplot.show()
print(len(X),"X-Length")

from sklearn.metrics import confusion_matrix

import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

# loading the iris dataset

from joblib import dump, load



data_set=None


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)


# dividing X, y into train and test data

def svmtrain(X,y):

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # svm_model_linear = SVC(kernel='linear', C=1).fit(X, y)
    svm_model_linear =knn.fit(X, y)o09opo09o9



    dump(svm_model_linear, 'filename.joblib')

    svm_predictions = svm_model_linear.predict(X_test)

    print(len(X_test))

    print(svm_predictions)

# model accuracy for X_test

    accuracy = svm_model_linear.score(X_test, y_test)

    print("accuracy"+str(accuracy))


# creating a confusion matrix

    cm = confusion_matrix(y_test, svm_predictions)

    print(cm)

# svmtrain(X, y)