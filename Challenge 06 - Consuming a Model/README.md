# Challenge 6: Consuming a Model

#### Real-Time Endpoint
![Real-Time Endpoint](../img/C6-2.png?raw=true "Real-Time Endpoint")

#### Batch Scoring Pipeline
![Batch Scoring Pipeline](../img/C6-1.png?raw=true "Batch Scoring Pipeline")

## Background

ML Models are typically consumed either in real-time or as part of batch-oriented workloads. 

- Real-time scenarios apply to cases where streaming data is generated that needs to be scored with a trained model at ultra-low latency – this is common in interactive user-facing applications and transaction-based systems. 

- Batch scenarios occur when collected data is scored at regular intervals with some delay – this is common in BI and reporting. 

Azure Machine Learning supports deployment of models for both real-time and batch scenarios. Moreover, resources can be easily scaled to meet the needs of the workload and integrating monitoring can be used to identify errors early on.

## Challenge Overview

In this challenge you will deploy your trained AutoML model derived from your manual AutoML run [Challenge 3] to a real-time managed online endpoint and use your deployed model to score sample data. 

As a second step you will complete and run a batch-scoring pipeline where a set of holdout data is scored with your trained model and saved as a dataset in Azure ML.

## Challenge Objectives

-	Deploy the model trained in your AutoML run from Challenge 3 to a real-time endpoint

    -	Navigate to the results from your previous AutoML run – this run should be named '<i>yourinitials</i>-automl-run' and can be found under the Jobs panel in the left sidebar menu.

    -	From the 'Overview' tab, find the best performing model under the 'Best model summary' tab and click into the model listed under 'Algorithm name'

    -	From the 'Deploy' widget, select the 'Web service' option and complete the wizard using the following configuration:
        -	<b>Endpoint name:</b> yourinitials-automl-rt-ep
        -	<b>Compute type:</b> Azure Container Instance
        -	<b>Enable authentication:</b> True
        -	<i>Use default no-code deployment settings</i>

    -	After the deployment has completed submit the following data to the endpoint using the Studio UI Test feature:
    ```
    {
        "Inputs": {
            "data": [
            {
                "CRIM": 0.0,
                "ZN": 0.0,
                "INDUS": 0.0,
                "CHAS": 0,
                "NOX": 0.0,
                "RM": 0.0,
                "AGE": 0.0,
                "DIS": 0.0,
                "RAD": 0,
                "TAX": 0,
                "PTRATIO": 0.0,
                "LSTAT": 0.0
            }
            ]
        }
    }
    ```

    -	<b>⭐Extra Credit⭐</b> Call the endpoint directly in code from a Jupyter notebook 

        -	<i>Hint: You may not need to generate Python code to call the API endpoint yourself – take a look under the Consume tab of the endpoint</i>

    -	Create a new AML dataset named '<i>YOURINITIALS</i>-HOME-PRICE-TEST-DATA' from the `BHP_Data_Test.csv` file in the Challenge 2 folder if you have not already done so.

    - 	Consume your trained AutoML model via a batch scoring pipeline

        -	Upload `AML_Pipeline_Creation.ipynb` and the `./pipeline_step_scripts` directory from this folder to your Azure ML environment.

        -	Update the default values for the PipelineParameters called `model_name`, `datastore_name`, `inferencing_dataset_name`, `scored_dataset_name` according to the instructions in the table below:


        | Pipeline Parameter Name |  Description |
        |-------------------------|--------------|
        | `model_name`  | The name of the model in your model registry which you will use for batch scoring (if you have completed Challenge 5 this should be the same value  you used for the `model_name` parameter there) |
        | `datastore_name` | The name of the datastore where your output dataset will be saved |
        | `inferencing_dataset_name` | The name of the test dataset you created ('<i>YOURINITIALS</i>-HOME-PRICE-TEST-DATA') |
        | `scored_dataset_name` | Name of the dataset to be created upon pipeline execution with your scored home price results |


        -	Run all cells of the notebook to run the pipeline. Upon completion locate the scored dataset in the Azure ML Studio.

            -	Identify the column containing ML model generated predictions



## Challenge-Specific Documentation

Use the documentation below as a reference when completing the tasks above. <i>Hint:</i> All the information required to complete these objectives is contained within these documents. 

- [What are Machine Learning Endpoints?](https://docs.microsoft.com/en-us/azure/machine-learning/concept-endpoints)

- [Create and Use Managed Online Endpoints in the Studio](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-managed-online-endpoint-studio)

- [Deploy an AutoML Model to an Online Endpoint](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-deploy-automl-endpoint?tabs=Studio)

- [Create and Use AML Environments](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-use-environments)

- [What are Azure Machine Learning Pipelines?](https://docs.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines)

- [Creating and Running Azure Machine Learning Pipelines](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-machine-learning-pipelines)
