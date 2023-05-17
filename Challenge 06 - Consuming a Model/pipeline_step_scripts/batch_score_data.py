# Import required packages
from azureml.core import Run, Datastore, Dataset
from azureml.core.model import Model
import pandas as pd
import argparse
from sklearn.externals import joblib

# #Parse input arguments
parser = argparse.ArgumentParser("Evaluate new model and register if more performant")
parser.add_argument('--model_name', type=str, required=True)
parser.add_argument('--datastore_name', type=str, required=True)
parser.add_argument('--inferencing_dataset_name', type=str, required=True)
parser.add_argument('--scored_dataset_name', type=str, required=True)

args, _ = parser.parse_known_args()
model_name = args.model_name
datastore_name = args.datastore_name
inferencing_dataset_name = args.inferencing_dataset_name
scored_dataset_name = args.scored_dataset_name

#Get current run
current_run = Run.get_context()

#Get parent run
parent_run = current_run.parent

#Get associated AML workspace
ws = current_run.experiment.workspace

#Get datastore
ds = Datastore.get(ws, datastore_name)

#Get inferencing dataset
inferencing_dataset = Dataset.get_by_name(ws, inferencing_dataset_name)
inferencing_df = inferencing_dataset.to_pandas_dataframe()

#Check that dataset does not contain actuals
try:
    inferencing_df = inferencing_df.drop(columns=['MEDV'])
except Exception:
    pass

#Retrieve model from workspace
aml_model = Model(ws, model_name)
aml_model.download('.', exist_ok=True)

# Load model into code
try:
    model = joblib.load('./outputs/model.pkl')
except Exception:
    model = joblib.load('model.pkl')

# Make predictions with model
predictions = model.predict(inferencing_df)

# Append predictions to inferencing dataset
inferencing_df['PREDICTIONS'] = predictions

# Create timestamp string
from datetime import datetime
timestamp = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")

# Register dataset in AML workspace
Dataset.Tabular.register_pandas_dataframe(inferencing_df, target = (ds, timestamp), name=scored_dataset_name)
