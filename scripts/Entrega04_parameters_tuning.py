import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier

# Load iris dataset
data = pd.read_csv("c:../datasets/UJIIndoorLoc/UJIIndoorLoc_ID.csv") 
data['ID'] = data['ID'].astype('category')
data['ID'] = data['ID'].cat.codes
X = data.drop(['ID'], axis=1)
y = data['ID']


print(data.info())
print('Class labels:', np.unique(data['ID']))
print('Labels counts in y:', np.bincount(data['ID']))

# StandardScaler
#std_scale = StandardScaler()
#X = std_scale.fit_transform(X)
#X = pd.DataFrame(X)

# Numerical to 0,1
#X[X == 100] = 0
#X[X < 0] = 1


#
# Brute force
#

# Unsupervised Features correlation 
# 

correlated_features = set()
_correlation_matrix = X.corr(method='spearman')
for i in range(len(_correlation_matrix.columns)):
    for j in range(i):
        if abs(_correlation_matrix.iloc[i, j]) > 0.8:
            _colname = _correlation_matrix.columns[i]
            correlated_features.add(_colname)

print("Unsupervised brute force")
print("Strong correlated features")
print(correlated_features)

# To remove selected features
#X = X.drop(labels=correlated_features, axis=1)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)



names = [
        "Nearest Neighbors", 
        #"Linear SVM", 
        #"Neural Net",
        #"Bagging"
        ]

classifiers = [
    KNeighborsClassifier(3),
    #SVC(kernel="linear", C=1),
    #MLPClassifier(alpha=1, max_iter=100),
    #BaggingClassifier(base_estimator=KNeighborsClassifier(3), n_estimators=10, bootstrap=True),
    ]



# iterate over classifiers
for name, clf in zip(names, classifiers):
    try:
        t1 = time.time()
        clf.fit(X_train, y_train)
        tTrain = time.time() - t1;
        t2 = time.time()
        y_pred = clf.predict(X_test)
        tTest = time.time() - t2;
        print(name) 
        print('Accuracy')
        print(str(accuracy_score(y_test, y_pred)))
        print('Training Time:%f s' % tTrain)
        print('Test Time %f s' % tTest)
    except ValueError:
        pass    


