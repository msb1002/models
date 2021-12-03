import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(np.array([1,2]))+3

model = LinearRegression().fit(X,y)
print(model.score())