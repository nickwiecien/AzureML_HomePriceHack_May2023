# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
import os
import pandas as pd

# Import MLFlow for tracking model performance
import mlflow

# Import argparse to parse command-line arguments
import argparse

# Import mltable to load input data
import mltable

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--inputs', type=str) # path to input data
parser.add_argument('--target_column', type=str) # name of target column
parser.add_argument('--test_percent', type=float) # percentage of data to use for testing
parser.add_argument('--model_name', type=str) # name of the trained model
args = parser.parse_args()

# Store parsed arguments in variables
inputs = args.inputs
target_column = args.target_column
test_percent = args.test_percent
model_name = args.model_name

# Load input data into a Pandas DataFrame
tbl = mltable.load(args.inputs)
df = tbl.to_pandas_dataframe()

# Split the data into training and testing sets
X = df.drop(target_column, axis=1) # features
y = df[target_column] # labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_percent)

# Enable automatic logging of parameters, metrics, and artifacts to MLflow
import mlflow.sklearn
mlflow.sklearn.autolog()

#Start a new MLflow run to track the training process
with mlflow.start_run() as run:
    run_id = run.info.run_id
    
    # Scale the data using MinMaxScaler and train a Random Forest Regressor model using Pipeline
    scaler = preprocessing.MinMaxScaler()
    clf = RandomForestRegressor()
    pipeline = Pipeline([('transformer', scaler), ('estimator', clf)])
    pipeline.fit(X_train, y_train)

    # Register the trained model with MLflow
    mlflow.register_model(f"runs:/{run_id}/model",model_name)