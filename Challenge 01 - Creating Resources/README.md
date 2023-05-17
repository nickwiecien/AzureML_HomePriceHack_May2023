# Challenge 1: Creating Resources

#### Compute Cluster
![Compute Cluster](../img/C1.png?raw=true "Compute Cluster")

#### Datastore
![Datastore](../img/C1-2.png?raw=true "Datastore")

## Background

Azure Machine Learning pulls together all the resources needed to support enterprise-scale data science initiatives in a single management plane. Compute and storage are essential elements to enabling ML model development.

## Challenge Overview

In this challenge you will navigate to your pre-provisioned Azure Machine Learning workspace, familiarize yourself with the Studio UI, and create compute & storage resources that will be used for the remainder of this hack. 

## Challenge Objectives

-	Navigate to your Azure Machine Learning resource in your team-assigned Azure resource group and launch the studio UI.

-	Locate the 'Learning Components' and 'Tutorials' section of the Studio for reference.

- ⚠️ <b>Note: If AML compute resources have already been provisioned you can skip the steps below. Review your compute resources in the AML Studio and start your compute instance, then and proceed to creating your datastore. </b>⚠️

    -	Create a Compute Instance named 'aml-ci-<i>yourinitials</i>' using a General Purpose <b>Standard_DS3_v2</b> virtual machine. 

        -	Set your compute instance to shut down on a schedule at 10 PM UTC or 5 PM US Central Time.

    -	Create a Compute Cluster named 'cpucluster-<i>yourinitials</i>' again using a General Purpose <b>Standard_DS3_v2</b> (Dedicated) virtual machine using the following configuration:
        -	<b>Minimum number of nodes:</b> 0
        -	<b>Maximum number of nodes:</b> 1
        -	<b>Idle seconds before scale down:</b> 300

-	From the Azure portal, navigate to the AML-linked storage account and create a new blob storage container named '<i>your-initials</i>-data'.

-	Register your newly created storage container as a datastore in your AML workspace as '<i>your-initials</i>_datastore'. <i><b>(Note: this is the location where you will upload home data for model training/testing)</b></i>.

## Challenge-Specific Documentation

Use the documentation below as a reference when completing the tasks above. <i>Hint:</i> All the information required to complete these objectives is contained within these documents. 

- [What is an Azure Machine Learning Compute Instance?](https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-instance)

- [Create Training/Deploy Computes (AML Studio)](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-create-attach-compute-studio)

- [Create and Manage a Compute Instance](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-create-manage-compute-instance?tabs=python)

- [Create Compute Clusters](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-create-attach-compute-cluster?tabs=python)

- [Connect to Data Storage with the Studio UI](https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-connect-data-ui?tabs=credential)

- [Manage Storage Account Access Keys (Azure Storage)](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal)