from sklearn import tree 
import pandas as pd
import numpy as np
from weather import temp

# import dataset
dataset = pd.read_csv('data.csv', sep=",", delimiter=None)

# define attribute and label data
x = dataset[['mintemp','maxtemp']]
y = dataset['clothing']

# decision tree classifier
clf = tree.DecisionTreeClassifier()

# train tree
model = clf.fit(x,y)

# retrieve temp values for model
temp_min = temp['temp_min']
temp_max = temp['temp_max']

# establish prediction value
predict = np.array([temp_min, temp_max])
predict = predict.reshape(1,-1)

# predict shorts or pants
prediction = clf.predict(predict)

# use joblib to persist model
from sklearn.externals import joblib

# save the file to the current working directory
joblib_file = "joblib_model.pk1"
joblib.dump(model, joblib_file)
