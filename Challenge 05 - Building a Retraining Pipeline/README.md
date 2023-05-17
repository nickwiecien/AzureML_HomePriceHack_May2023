# Challenge 5: Build a Model Training Pipeline

#### Pipeline Run
![Pipeline Run](../img/C5.png?raw=true "Pipeline Run")

## Background

Supporting ML models in production requires regular retraining. ML models perform well when the future looks like the past, but as trends change and data drifts model performance can erode. 

To combat this and keep models performing well in production regular retraining using up-to-date data is essential – this is a MLOps best practice. 

Azure Machine Learning pipelines are reusable software constructs that make it easy to automatically retrieve updated datasets, train new models, and quantitatively compare performance against previous models. These pipelines can be triggered on either a schedule or event-driven basis.

## Challenge Overview

In this challenge you will create a retraining pipeline to create new versions of your home price prediction model leveraging up-to-date data from your datastore. 

Additionally, you will implement logic to perform an A/B (champion vs. challenger) test to compare performance of your newly trained model against a previous version.

## Challenge Objectives

-	Upload `AML_Pipeline_Creation.ipynb` and the `./pipeline_step_scripts` directory from this folder to your Azure ML environment.

-	Update `AML_Pipeline_Creation.ipynb` with the following components where indicated:

    -	Create a custom environment from the attached `automl_env.yaml` file named 'yourinitials-automl-env'

    -	Update the default values for the PipelineParameters called `datastore_name`, `data_path`, `model_name`, `training_percentage` with a values corresponding to the table below. 

    -	Update the AutoMLConfig object to include the following settings:
        -	<b>Maximum allowed run time:</b> 30 minutes
        -	<b>Allowed Models:</b> XGBRegressor, LightGBM
        -	<b>Cross-Validation:</b> k-folds with 3 separate folds
        -	<b>Max Concurrent Iterations:</b> 1

-	Find the syntax for creating an Azure Machine Learning pipeline and create a pipeline under the variable named `pipeline`.

-	Use the helper function `create_pipeline_endpoint()` to publish your ML pipeline to a PipelineEndpoint (Note: PipelineEndpoints expose consistent REST APIs which can be triggered remotely to support event-driven execution).

    -	After publishing your pipeline to a PipelineEndpoint, navigate to this asset in the Studio UI. 

-	Update `./pipeline_step_scripts/get_data.py` with the following components where indicated:

    -	Update the `datastore` and `dataset` variables to leverage the parameters passed into the python script.

    -	Use scikit-learn’s `train_test_split()` function to split data into test and training sets.
    

## Challenge-Specific Documentation

Use the documentation below as a reference when completing the tasks above. <i>Hint:</i> All the information required to complete these objectives is contained within these documents. 

- [What are Azure Machine Learning Pipelines?](https://docs.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines)

- [Creating and Running Azure Machine Learning Pipelines](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-machine-learning-pipelines)

- [Moving Data in AML Pipelines](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-move-data-in-out-of-pipelines)

- [Azure Machine Learning Curated Environments](https://docs.microsoft.com/en-us/azure/machine-learning/resource-curated-environments)

- [Using AutoML in Pipelines](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-automlstep-in-pipelines)

- [DataPath and PipelineParameter Sample](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/intro-to-pipelines/aml-pipelines-showcasing-datapath-and-pipelineparameter.ipynb)

- [AutoMLStep](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps.automl_step.automlstep?view=azure-ml-py)

- [AutoMLConfig](https://docs.microsoft.com/en-us/python/api/azureml-train-automl-client/azureml.train.automl.automlconfig.automlconfig?view=azure-ml-py)