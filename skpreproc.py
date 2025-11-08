import numpy as np
from sklearn import preprocessing
Input_data = np.array(
   [[2.1, -1.9, 5.5],
   [-1.5, 2.4, 3.5],
   [0.5, -7.9, 5.6],
   [5.9, 2.3, -5.8]]
)
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(Input_data)
print("\nBinarized data:\n", data_binarized)

#displaying the mean and the standard deviation of the input data
print("Mean =", Input_data.mean(axis=0))
print("Stddeviation = ", Input_data.std(axis=0))
#Removing the mean and the standard deviation of the input data

data_scaled = preprocessing.scale(Input_data)
print("Mean_removed =", data_scaled.mean(axis=0))
print("Stddeviation_removed =", data_scaled.std(axis=0))

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(Input_data)
print ("\nMin max scaled data:\n", data_scaled_minmax)

data_normalized_l1 = preprocessing.normalize(Input_data, norm='l1')
print("\nL1 normalized data:\n", data_normalized_l1)

data_normalized_l2 = preprocessing.normalize(Input_data, norm='l2')
print("\nL2 normalized data:\n", data_normalized_l2)