import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
class ModelTraining:
    def KNN_Mid2(self, df: pd.DataFrame):
        # Calculate the sum of the first four assignments and quizzes
        df['Sum_Assignments'] = df[['As:1', 'As:2', 'As:3', 'As:4']].sum(axis=1)
        df['Sum_Quizzes'] = df[['Qz:1', 'Qz:2', 'Qz:3', 'Qz:4']].sum(axis=1)

        # Split the data into features (X) and target variable (y)

        #     X = df[['As:1', 'As:2', 'As:3', 'As:4', 'Qz:1', 'Qz:2', 'Qz:3','Qz:4', 'S-I']]
        #     y = df['Grade']

        X = df[['Sum_Assignments', 'Sum_Quizzes', 'S-I']]
        y = df['Grade']

        # Encode the target variable
        le = LabelEncoder()
        y = le.fit_transform(y)

        # Split the data into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create KNN classifier with k=4
        knn = KNeighborsClassifier(n_neighbors=4)

        # Train the model using the training sets
        knn.fit(X_train, y_train)

        # Make predictions on the testing set
        y_pred = knn.predict(X_test)

        # Evaluate the model
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=le.classes_))

        # Calculate accuracy score
        accuracy = accuracy_score(y_test, y_pred)

        # Print accuracy in percentage
        print(f"Accuracy: {accuracy * 100:.2f}%")



    # Prediction using KNN after mid2
    def KNN_Finals(self, df : pd.DataFrame):

        # Split the data into features (X) and target variable (y)
        X = df[['As', 'Qz', 'S-I', 'S-I']]
        y = df['Grade']

        # Encode the target variable
        le = LabelEncoder()
        y = le.fit_transform(y)

        # Split the data into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create KNN classifier with k=4
        knn = KNeighborsClassifier(n_neighbors=4)

        # Train the model using the training sets
        knn.fit(X_train, y_train)

        # Make predictions on the testing set
        y_pred = knn.predict(X_test)

        # Evaluate the model
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=le.classes_))

        # Calculate accuracy score
        accuracy = accuracy_score(y_test, y_pred)

        # Print accuracy in percentage
        print(f"Accuracy: {accuracy * 100:.2f}%")

    # Prediction using Decision Tree before mid2
    def DecisionTree_Mid2(self, df : pd.DataFrame):

        # Calculate the sum of the first four assignments and quizzes
        df['Sum_Assignments'] = df[['As:1', 'As:2', 'As:3', 'As:4']].sum(axis=1)
        df['Sum_Quizzes'] = df[['Qz:1', 'Qz:2', 'Qz:3', 'Qz:4']].sum(axis=1)

        # Split the data into features (X) and target variable (y)
        X = df[['Sum_Assignments', 'Sum_Quizzes', 'S-I']]
        y = df['Grade']

        # Encode the target variable
        le = LabelEncoder()
        y = le.fit_transform(y)

        # Split the data into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create Decision Tree classifier
        dt = DecisionTreeClassifier()

        # Train the model using the training sets
        dt.fit(X_train, y_train)

        # Make predictions on the testing set
        y_pred = dt.predict(X_test)

        # Evaluate the model
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=le.classes_))

        # Calculate accuracy score
        accuracy = accuracy_score(y_test, y_pred)

        # Print accuracy in percentage
        print(f"Accuracy: {accuracy * 100:.2f}%")

    # Prediction using Decision Tree after mid2
    def DecisionTree_Finals(self, df : pd.DataFrame):

        # Split the data into features (X) and target variable (y)
        X = df[['As', 'Qz', 'S-I', 'S-II']]
        y = df['Grade']

        # Encode the target variable
        le = LabelEncoder()
        y = le.fit_transform(y)

        # Split the data into training and testing sets (80% training, 20% testing)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create Decision Tree classifier
        dt = DecisionTreeClassifier()

        # Train the model using the training sets
        dt.fit(X_train, y_train)

        # Make predictions on the testing set
        y_pred = dt.predict(X_test)

        # Evaluate the model
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=le.classes_))

        # Calculate accuracy score
        accuracy = accuracy_score(y_test, y_pred)

        # Print accuracy in percentage
        print(f"Accuracy: {accuracy * 100:.2f}%")