from sklearn.externals import joblib
from weather import temp
import numpy as np

# load model from file
joblib_file = "joblib_model.pk1"
joblib_model = joblib.load(joblib_file)

# retrieve temp values for model
temp_min = temp['temp_min']
temp_max = temp['temp_max']

# establish prediction value
predict = np.array([temp_min, temp_max])
predict = predict.reshape(1,-1)

# predict shorts or pants
prediction = joblib_model.predict(predict)

print(prediction)
