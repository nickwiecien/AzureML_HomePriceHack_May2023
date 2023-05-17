# Import required packages
from azureml.core import Run, Workspace, Datastore, Dataset
from azureml.core.model import Model
from azureml.data.datapath import DataPath
import pandas as pd
import os
import argparse
import shutil
from sklearn.externals import joblib
from sklearn.metrics import mean_squared_error

# #Parse input arguments
parser = argparse.ArgumentParser("Evaluate new model and register if more performant")
parser.add_argument('--model_name', type=str, required=True)

args, _ = parser.parse_known_args()
model_name = args.model_name

#Get current run
current_run = Run.get_context()

#Get parent run
parent_run = current_run.parent

#Get associated AML workspace
ws = current_run.experiment.workspace

#Get default datastore
ds = ws.get_default_datastore()

#Get testing dataset
test_datset = current_run.input_datasets['testing_dataset']
test_df = test_datset.to_pandas_dataframe()

#Separate inputs from outputs (actuals). Create separate dataframes for testing champion and challenger.
actuals = test_df[['MEDV']]
test_X1 = test_df.drop('MEDV', axis=1)
test_X2 = test_df.drop('MEDV', axis=1)

#Get updated 'challenger' model
for c in parent_run.get_children():
    if 'AutoML' in c.name:
        best_child_run_id = c.tags['automl_best_child_run_id']
        automl_run = ws.get_run(best_child_run_id)
        automl_run.download_files('outputs', output_directory='challenger_outputs', append_prefix=False)
        challenger_model = joblib.load('challenger_outputs/model.pkl')
        print(os.listdir('challenger_outputs'))
        print()
        print(best_child_run_id)
        print()
        challenger_tags = {'Parent Run ID': parent_run.id, 'AutoML Run ID': best_child_run_id}
        
#Calculate challenger metrics
challenger_preds = challenger_model.predict(test_X1)
challenger_rms = mean_squared_error(actuals, challenger_preds, squared=False)
challenger_metric = challenger_rms/(actuals['MEDV'].max()-actuals['MEDV'].min())
challenger_tags['Target Metric (Normalized RMSE)']=challenger_metric
challenger_tags['Comparison Metric (Normalized RMSE)'] = -1.0
    
#Check if no model is registered
if len(Model.list(ws, name=model_name))==0:
    #If no model is registered, register newly trained model by default
    import os
    os.rename('challenger_outputs', 'outputs')
    Model.register(model_path="outputs",
                          model_name=model_name,
                          tags=challenger_tags,
                          description="Boston Home Prices Prediction Model",
                          workspace=ws)
else:
    #Otherwise, import the incumbent model and test against the current test dataset
    Model(ws, name=model_name).download(target_dir='champion_outputs', exist_ok=True)
    champion_model = joblib.load('champion_outputs/outputs/model.pkl')
    champion_preds = champion_model.predict(test_X2)
    print(challenger_preds)
    print()
    print(champion_preds)
    print()
    print(os.path.getsize('challenger_outputs/model.pkl'))
    print(os.path.getsize('champion_outputs/outputs/model.pkl'))
    champion_rms = mean_squared_error(actuals, champion_preds, squared=False)
    champion_metric = champion_rms/(actuals['MEDV'].max()-actuals['MEDV'].min())
    
    print('Champion: ' + str(champion_metric))
    print('Challenger: ' + str(challenger_metric))
    
    # If new model does not perform better cancel the run
    if champion_metric <= challenger_metric:
        print('New model does not perform better than existing model. Cancel run.')
        current_run.parent.cancel()
    else:
        # If new model does perform better, add it to the registry
        challenger_tags['Comparison Metric (Normalized RMSE)'] = champion_metric
        import os
        os.rename('challenger_outputs', 'outputs')
        Model.register(model_path="challenger_outputs",
                              model_name=model_name,
                              tags=challenger_tags,
                              description="Boston Home Prices Prediction Model",
                              workspace=ws)