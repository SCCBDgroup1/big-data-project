import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

# Load iris dataset
data = pd.read_csv("c:../datasets/UJIIndoorLoc/UJIIndoorLoc_B0-ID-01.csv") 
data['ID'] = data['ID'].astype('category')
data['ID'] = data['ID'].cat.codes

print(data.info())

# Split in train and test datasets
# 2D Attributes
X = data.drop(['ID'], axis=1)
y = data['ID']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
labels =  np.unique(y)
labels_count = np.bincount(y)
labels_train_count = np.bincount(y_train)
labels_test_count = np.bincount(y_test)

names = ["Nearest Neighbors", "Decision Tree", "Naive Bayes", "Linear SVM", "RBF SVM", "Neural Net"]

classifiers = [
    KNeighborsClassifier(3),
    DecisionTreeClassifier(max_depth=100),
    GaussianNB(),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    MLPClassifier(alpha=1, max_iter=1000)]

metrics = pd.DataFrame(columns=names, index=['Accuracy'])

# iterate over classifiers
for name, clf in zip(names, classifiers):
    clf.fit(X_train, y_train)
    metrics.at['Accuracy', name] = clf.score(X_test, y_test)
    

export_csv = metrics.to_csv (r'c:../scripts/02_classifiers_results.csv', index = True, header=True)
