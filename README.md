# StudentGradePredictor

## Overview
This project aims to predict whether a student will pass or fail based on their performance in assignments, quizzes, and sessional marks. Two different cases are considered for prediction:
1. **Case 1:** Predict grade using the marks of the first 4 assignments, 4 quizzes, and Sessional 1 marks.
2. **Case 2:** Predict grade using the marks of the best 5 assignments, 5 quizzes, and Sessional 1 and 2 marks.

## Dataset
The dataset file contains information about student performance in assignments, quizzes, and sessional marks.

## Project Structure
The project is structured into several modules to perform various tasks:
- `data_preprocess.py`: Module for normalizing data (assignment and quiz marks) and merging sheets in the dataset file.
- `data_analysis.py`: Module for performing summary analysis and exploratory data analysis (EDA).
- `model_training.py`: Module for training and using K-Nearest Neighbors (KNN) and Decision Tree classifiers to predict grades.

## Steps to Run the Project
1. **Normalize the Data**
   - Use `DataPreprocessing Class` to normalize assignment and quiz marks in the dataset.
2. **Merge Sheets**
   - Use `DataPreprocessing Class` to merge sheets in the dataset file and create a new file.
3. **Perform Summary Analysis**
   - Use `DataAnalysis Class` to perform a summary analysis on the merged dataset.
4. **Perform EDA**
   - Use `DataAnalysis Class` to perform exploratory data analysis (EDA) on the merged dataset.
5. **Train and Test Models**
   - Use `ModelTraining Class` to train and test KNN and Decision Tree classifiers for grade prediction.

## Dependencies
- Python 3.x
- Required Python libraries (pandas, matplotlib, scikit-learn, tk)

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the project by executing the `main.py` Python file.

## Results
After running the project, you can analyze the results of grade prediction using KNN and Decision Tree classifiers for both Case 1 and Case 2.
