from sklearn import tree 
import pandas as pd
import numpy as np

# import dataset
dataset = pd.read_csv('data.csv', sep=",", delimiter=None)
# print(dataset)

# define attribute and label data
x = dataset[['mintemp','maxtemp']]
#print(x)

y = dataset['clothing']
#print(y)

# decision tree classifier
clf = tree.DecisionTreeClassifier()

# train tree
train = clf.fit(x,y)

# establish prediction value
predict = np.array([30, 40])
predict = predict.reshape(1,-1)

# predict shorts or pants
prediction = clf.predict(predict)

print(prediction)
