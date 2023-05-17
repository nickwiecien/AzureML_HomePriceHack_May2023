# Challenge 4: Creating an Experiment and Submitting a Run

#### ScriptRun Results
![ScriptRun Results](../img/C4.png?raw=true "ScriptRun Results")

## Background

Within Azure ML Experiments are logical collections of individual script executions – these scripts can be for data preparation, model training, and/or inferencing activities. 

Scripts can be run in different environments and using different types of compute – useful for right-sizing your resources to the task at hand. Additionally, within individual Runs you can log metrics and store artifacts from your script execution. 

As you iterate on model development or data preparation activities, experiment/run tracking is useful for quickly making comparisons between different iterations to check for performance improvements.

To this end, [MLflow](https://mlflow.org/) is an extremely useful open-source framework for tracking ML experiments and saving model artifacts in a standardized format making them easy to package and deploy in different environments. MLflow integrates natively with Azure Machine Learning and workspaces can be used in the same way as MLflow tracking servers. [Read more about MLflow integration with Azure Machine Learning here](https://learn.microsoft.com/en-us/azure/machine-learning/concept-mlflow).

## Challenge Overview

In this challenge you will take a prepared script `train.py` and submit it as a ScriptRun within your AML workspace using the `Submit_Run.ipynb` sample notebook. This script utilizes a Scikit-Learn random forest model trained as part of an MLflow run.

In the previous step your environment was automatically configured and metrics logged automatically via AutoML. Here, you will carry these activities out manually. 

To achieve the objectives below you will need to make modifications to the provided code where indicated. Note: the documentation below will be <i>EXTREMELY</i> helpful for this challenge.

## Challenge Objectives

-	Upload `train.py`, `sklearn_env.yml`, and `Submit_Run.ipynb` to your Azure ML environment. (Note: this can be done via drag-and-drop in JupyterLab which we recommend as a notebook-based IDE).

-	Update `Submit_Run.ipynb` with the following components where indicated:

    -	Create an experiment named '<i>your-initials</i>_home_price_model_training_custom_script'

    -	Get a reference to your compute cluster as the variable compute_target – this will be used for your script submission
    -	Create a reusable Azure ML environment from the uploaded `sklearn_env.yml` file. <i>Note: For our experiment we are using an previously curated conda yaml file to create our reusable environment. We can alternatively provide pip requirement files or specify packages/versions manually.</i>
  
-	Update `train.py` with the following components where indicated:

    -	Access your previously created dataset (Challenge 2) from the AML workspace and load as a pandas dataframe 

    -	Add the computed metrics for mean absolute error (MAE) and root mean squared error (RMSE) to your run 

    -	Add the residuals histogram/scatterplot generated from matplotlib to your run as images

    -	Register the model (named '<i>yourinitials</i>-home-price-model') in your AML workspace


## Challenge-Specific Documentation

Use the documentation below as a reference when completing the tasks above. <i>Hint:</i> All the information required to complete these objectives is contained within these documents. 

- [Create and Submit Training Runs](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-set-up-training-targets)

- [Log and View Metrics and Files](https://docs.microsoft.com/en-us/azure/machine-learning/v1/how-to-log-view-metrics)

- [Track ML models with MLflow and Azure Machine Learning](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-use-mlflow?tabs=azuremlsdk)

- [Create and Use AML Environments](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-use-environments)