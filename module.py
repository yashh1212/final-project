import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def predict(a):
    # Load the CSV data into a Pandas DataFrame
    heart_data = pd.read_csv("heart.csv") 

    # Display basic data information
    print("First five rows of dataset:")
    print(heart_data.head())
    print("\nLast five rows of dataset:")
    print(heart_data.tail())
    print("\nData shape:")
    print(heart_data.shape)
    print("\nMissing values:")
    print(heart_data.isnull().sum())
    print("\nStatistical measures:")
    print(heart_data.describe())
    print("\nDistribution of the target variable:")
    print(heart_data['target'].value_counts())

    # Split the features and target
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']

    # Split the data into training and test sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    # Model training using logistic regression
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # Model evaluation
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
    print("Accuracy on training data:", training_data_accuracy)

    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
    print("Accuracy on test data:", test_data_accuracy)

    # Building a predictive system
    # input_data = []
    # features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'resting', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    # for feature in features:
    # input_data.append(float(input(f"Enter {feature}: ")))

    input_data_as_numpyarray = np.array(a).reshape(1, -1)
    prediction = model.predict(input_data_as_numpyarray)

    if prediction[0] == 0:
        return "The person does not have heart disease."
    else:
        return "The person has heart disease."
print(predict())
