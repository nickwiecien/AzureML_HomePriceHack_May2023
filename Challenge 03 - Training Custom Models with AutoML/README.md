# Challenge 3: Training Custom Models with AutoML

#### AutoML Results
![AutoML Results](../img/C3.png?raw=true "AutoML Results")

## Background

ML model development can be an iterative and time-consuming process entailing multiple rounds of model selection and hyperparameter tuning on the path to building a model that can predict target values with high-accuracy. 

Historically, training high-performing models has necessitated deep familiarity with multiple different types of ML models and their associated hyperparameters, data preprocessors, and routines for tuning these settings. 

The advent of automated ML (or AutoML for short) technologies has lowered this bar dramatically. Leverage their own ML capabilities under-the-hood, AutoML tools allow users to simply provide datasets with target outputs, and then they evaluate multiple different combinations of feature engineering, model selection, and hyperparameter settings to find the best performing model for a given dataset/ML task.

Azure Machine Learning’s AutoML supports functionality for training classic regression, classification, and time-series forecasting models and recently additional capabilities for training custom computer vision and natural language processing models. 

Using AML’s AutoML capabilities allows you to train custom models on your data - without having to reason over different model/featurization approaches – and will intelligently identify the best performer for your particular scenario.

## Challenge Overview

In this challenge you will train a custom regression model to predict home prices using the datasets and compute resources created in the previous two challenges. To train your custom model you will leverage AML’s AutoML functionality either through the Studio UI or AML Python SDK - in a later challenge you will leverage the SDK so we recommend using the Studio UI for this portion.

## Challenge Objectives

-	Submit an AutoML run using either the Studio UI or AML SDK with the following configuration:
    -   <b>Experiment Name:</b> <i>yourinitials</i>-automl-run
    -   <b>Target Column:</b> MEDV
    -   <b>Compute Cluster:</b> cpucluster
    -   <b>Model Type:</b> Regression
    -	<b>Training Time (hours):</b> 0.5
    -	<b>Allowed Models:</b> XGBoostRegressor, LightGBM
    -	<b>Max Concurrent Iterations:</b> 1 (❗Make sure to adjust this setting this to ensure available cluster capacity❗)
    -	<b>Cross-Validation:</b> K-Fold Cross-Validation with 3 separate folds
    -	<i>Note:</i> Model training will likely take 15-30 minutes for this step and is a good opportunity to help your peers, stretch your legs, and grab some coffee ☕!

-	Locate model performance metrics within your experiment record

-	Score the data located within `BHP_Data_Test.csv` file from Challenge #2 and for extra credit compute/review performance metrics of your choice by comparing actuals to predictions.


## Challenge-Specific Documentation

Use the documentation below as a reference when completing the tasks above. <i>Hint:</i> All the information required to complete these objectives is contained within these documents. 

- [What is Automated ML?](https://docs.microsoft.com/en-us/azure/machine-learning/v1/concept-automated-ml-v1)

- [Tutorial: AutoML-Train No-Code Models](https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-first-experiment-automated-ml)

- [Set up AutoML with Python](https://docs.microsoft.com/en-us/azure/machine-learning/v1/how-to-configure-auto-train-v1)

- [Tutorial: AutoML-Train Regression Model](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-auto-train-models-v1)