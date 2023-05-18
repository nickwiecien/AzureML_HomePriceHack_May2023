# Import required packages
from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np

#Parse input arguments
parser = argparse.ArgumentParser("Get data from attached datastore (Blob Storage), split into train and test subsets, and register in AML workspace")
parser.add_argument('--training_data', dest='training_data', required=True)
parser.add_argument('--testing_data', dest='testing_data', required=True)
parser.add_argument('--datastore_name', type=str, required=True)
parser.add_argument('--data_path', type=str, required=True)
parser.add_argument('--training_percentage', type=float, required=True)

args, _ = parser.parse_known_args()
training_data = args.training_data
testing_data = args.testing_data
datastore_name = args.datastore_name
data_path = args.data_path
training_percentage = args.training_percentage

#Get current run
current_run = Run.get_context()

#Get associated AML workspace
ws = current_run.experiment.workspace

#Connect to default Blob Store
ds = ws.get_default_datastore()

#TO-DO: GET REFERENCE TO YOUR DATASTORE (`datastore_name`) AND LOAD CSV DATA INTO PANDAS DATAFRAME FROM `data_path`
my_datastore = Datastore.get(ws, datastore_name)
csv_locations = (my_datastore, data_path)
tabular_dataset = Dataset.Tabular.from_delimited_files(path=csv_locations)
raw_df = tabular_dataset.to_pandas_dataframe()

train_df, test_df = train_test_split(raw_df, train_size=training_percentage)

#Make directory on mounted storage
os.makedirs(training_data, exist_ok=True)
os.makedirs(testing_data, exist_ok=True)

#Upload dataframes
train_df.to_csv(os.path.join(training_data, 'training_data.csv'), index=False)
test_df.to_csv(os.path.join(testing_data, 'testing_data.csv'), index=False)