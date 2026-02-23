import pandas as pd
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv(r'C:\Users\b9367\Downloads\gpa_study_hours.csv')
# here we read the csv file and store it in a variable called df
x=df[['study_hours']]
y=df['gpa']
# here we seperate the feature and target variable and store them in x and y respectively
model=DecisionTreeRegressor()
# here we create an instance of the DecisionTreeRegressor class and store it in a variable callwd model
model.fit(x,y)
# here we fit the model to the data by calling the fit and passing x and y as arguments
hours=float(input('enter study_hours :'))
# we take input from the user and store it in avariable called hours and convert into float data type
print(model.predict([[hours]]))