from azureml.core import Run, Workspace, Datastore, Dataset, Model
from azureml.data.datapath import DataPath
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import preprocessing
from sklearn.pipeline import Pipeline
import os
import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
import mlflow
import mlflow.sklearn

# Get current run
current_run = Run.get_context()

#Get associated AML workspace
ws = current_run.experiment.workspace

# TO-DO: LOAD DATASET AS PANDAS DATAFRAME
dataset_name = 'NWK-HOME-PRICE-DATA'
dataset = Dataset.get_by_name(ws, dataset_name)
dataset_df = dataset.to_pandas_dataframe()

# Split data into test and train subsets
train_df, test_df = train_test_split(dataset_df, test_size=0.8, shuffle=True)

# Specify target column
target_column = 'MEDV'

# Split data into X/y subsets
X_train = train_df.drop(target_column, axis=1)
X_test = test_df.drop(target_column, axis=1)
y_train = train_df[[target_column]]
y_test = test_df[[target_column]]

#Start a new MLflow run to track the training process
with mlflow.start_run() as run:
    run_id = run.info.run_id
    
    # Scale the data using MinMaxScaler and train a Random Forest Regressor model using Pipeline
    scaler = preprocessing.MinMaxScaler()
    clf = RandomForestRegressor()
    pipeline = Pipeline([('transformer', scaler), ('estimator', clf)])
    pipeline.fit(X_train, y_train)
    
    # TO-DO: CALCULATE MEAN ABSOLUTE ERROR & ROOT MEAN SQUARED ERROR USING TEST DATA
    # Hint: See https://scikit-learn.org/0.22/modules/classes.html#module-sklearn.metrics 
    preds = pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = sqrt(mean_squared_error(y_test, preds))
    mlflow.log_metric('Mean Absolute Error', mae)
    mlflow.log_metric('Root Mean Squared Error', rmse)
    
    # TO-DO: GENERATE RESIDUALS PLOT AND SAVE TO RUN USING MATPLOTLIB
    # Hint: Residuals = Actual (y_test) - Predicted (preds)
    residuals = [list(y_test.values)[i] - list(preds)[i] for i in range(len(y_test.values))]
    
    # Plot the residuals
    fig, ax = plt.subplots()
    ax.scatter(preds, residuals)
    ax.set_xlabel('Predicted values')
    ax.set_ylabel('Residuals')
    ax.set_title('Residuals vs. Predicted values')
    mlflow.log_figure(fig, 'residuals_plot.png')
    
    # Log the model to your run
    mlflow.sklearn.log_model(pipeline, 'model')

    # TO-DO: REGISTER YOUR TRAINED MODEL INTO THE WORKSPACE USING MLFLOW
    model_name = 'nwk-home-price-model'
    mlflow.register_model(f"runs:/{run_id}/model",model_name)

