# Challenge 7: Scheduling a Pipeline Run

#### Scheduled Pipeline Run
![Scheduled Pipeline Run](../img/C7.png?raw=true "Scheduled Pipeline Run")

## Background

ML models work wonderfully when the future looks exactly like the past. Unfortunately, this is rarely (if ever) the case and data tends to drift over time. 

As data drifts, the data which ML models were initially trained with becomes less representative of the current state. To combat this and ensure strong continued of our performance we can set up routines to automatically train our models using the most up-to-date data available. 

Regular retraining is considered an MLOps best practice and can be triggered either on a schedule or on an event-driven basis (e.g., when data drift is quantified and determined to be beyond an acceptable threshold).

## Challenge Overview

In this challenge you will leverage the AML SDK to set up your published model training pipeline to run on a schedule. 

<b>Note:</b> the pipeline you created is set up to retrieve all data from a particular datastore location. This is a strong design for production scenarios where new data is regularly added to a datastore.

## Challenge Objectives

-	In the AML Studio navigate to the PipelineEndpoint you created in Challenge 5 and verify the name (should be '<i>YOURINITIALS</i>-PipelineEndpoint')

-   Create a new Jupyter notebook in your AML workspace and create a connection to your AML workspace (<b>Hint:</b> Look at your previous notebooks for reference if you get stuck!)

-   Retrieve a reference to your `PipelineEndpoint` by updating and running the command below:


```
from azureml.pipeline.core import PipelineEndpoint

pipeline_endpoint = PipelineEndpoint.get(
    workspace=ws, name="<YOUR-PIPELINE-ENDPOINT-NAME>"
)
```


-   Create a `ScheduleRecurrence` object that is set up to run once a week starting 10 minutes from now in your current time zone. Modify the code block below accordingly. (<b>Hint:</b> Look at the [ScheduleRecurrence](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.schedulerecurrence?view=azure-ml-py) and [TimeZone](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.timezone?view=azure-ml-py) SDK docs for reference and samples).


```
from azureml.pipeline.core import ScheduleRecurrence, TimeZone
recurrence = ScheduleRecurrence(frequency="Week", interval=1, time_zone=TimeZone.CentralStandardTime)
```


-   Using your retrieved `PipelineEndpoint` and `ScheduleRecurrence` objects, create a `Schedule` using the syntax below with updated schedule and experiment names. 

    -   🚨<b>Note</b>🚨 Before executing this command, verify that your `ScheduleRecurrence` is set up to trigger 5 minutes from the current time - this is critical for ensuring your schedule has been set up properly.


```
from azureml.pipeline.core import Schedule
schedule = Schedule.create_for_pipeline_endpoint(ws, name='<YOUR-INITIALS-SCHEDULE>', pipeline_endpoint_id=pipeline_endpoint.id,experiment_name="<YOUR-INITIALS-SCHEDULEDRUN>", recurrence=recurrence)
```

-   To verify schedule creation you can run the command below:

```
Schedule.get_schedules_for_pipeline_endpoint_id(ws, pipeline_endpoint.id)
```

-   You can enable and disable scheduled jobs by calling `disable()` and `enable()`, respectively, on `Schedule` objects.

-   In <5 minutes you should see a new job called '<i>YOUR-INITIALS</i>-SCHEDULEDRUN' execute in the Studio.


## Challenge-Specific Documentation

Use the documentation below as a reference when completing the tasks above. <i>Hint:</i> All the information required to complete these objectives is contained within these documents. 

- [Trigger a Machine Learning Pipeline](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-trigger-published-pipeline)

- [Schedule](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.schedule(class)?view=azure-ml-py)

- [ScheduleRecurrence](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.schedulerecurrence?view=azure-ml-py)

- [TimeZone](https://docs.microsoft.com/en-us/python/api/azureml-pipeline-core/azureml.pipeline.core.timezone?view=azure-ml-py)
