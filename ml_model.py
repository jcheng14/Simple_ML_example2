#Date July 3rd, I opened the Python file using Nano, 
#And I only add a comment into the Python file
from sklearn.linear_model import LinearRegression

#Create sample training data
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

#Train the model
model = LinearRegression()
model.fit(X,y)

#Make predictions
X_test = [[6], [7]]
y_pred = model.predict(X_test)

print(y_pred)
