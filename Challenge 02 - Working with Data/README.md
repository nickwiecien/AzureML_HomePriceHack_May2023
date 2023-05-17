# Challenge 2: Working with Data

#### Dataset
![Dataset](../img/C2.png?raw=true "Dataset")

## Background

Azure Machine Learning supports creation and registration (read: saving and versioning) or datasets from multiple different data sources (Azure storage locations, online dataset, local files, etc.). These versioned datasets can then be explored and consumed in ML pipelines for model training and scoring.

## Challenge Overview

In this challenge you will create multiple versions of your home prices dataset using data located in this directory. After creating your datasets you will explore the statistical profile of your data and then load your data into code to display in a Jupyter notebook.

## Challenge Objectives

-	Download all files from this directory to your local machine. Note: you can pull the entire repository or download files individually by navigating to them, clicking 'Raw', and right-clicking to get to 'Save As'. There are multiple files from this repo that will be used throughout the hack so we recommend downloading the entire repository (this can be done by downloading a zipped dir from the repo home page).

-	Create a Tabular dataset named '<i>YOURINITIALS</i>-HOME-PRICE-DATA' from the `BHP_Data_01.csv` and `BHP_Data_02.csv` files. (Note: upload these data to your newly created datastore `yourinitials_datastore` and use the Azure ML v1 APIs during creation).

-	Find and explore the statistical profile of your newly created dataset. 

-	From your newly created Compute Instance launch JupyterLab and load the `Challenge_02.ipynb` notebook from this repo into your user folder.

-	Launch the uploaded notebook and update the code in Cell #2 to display your dataset directly in code.

## Challenge-Specific Documentation

Use the documentation below as a reference when completing the tasks above. <i>Hint:</i> All the information required to complete these objectives is contained within these documents. 

- [Connect to Data Storage with the Studio UI](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-connect-data-ui?tabs=credential)

- [Create Azure Machine Learning Datasets](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-create-register-datasets)