
# Predicting Opioid Overdose in DC

#### Team Members:  Dave Cook, Caroline Egan, Wranga Mujadidi, Sara Parker

**Domain:**  Government / Health

**Abstract :**  Drug overdose is the leading cause of accidental death in the US, with 52,404 lethal drug overdoses in 2015. Opioid addiction is driving this epidemic, with 20,101 overdose deaths related to prescription pain relievers, and 12,990 overdose deaths related to heroin in 2015 (CDC, ASAM). Adequate distribution and administration of narcan (naloxone HCl) is key to lowering mortality due to opiate overdose. 

In this study, our team uses classification machine learning models to predict which areas in DC are most likely to utilize narcan. Our model is trained on 2016 narcan administration data calls for service data provided by DC government’s Office of Unified Communications.

**Hypothesis: ** 

#### Overview

**Data Sources: **
2016 DC Narcan Administration Data
2016 DC Calls for Service
2016 DC Weather Data. 
   
**Data: **
Data includes Narcan administered informaiton and calls for service information.  The data was summarized by 500 meter hexagons that overlay 
with DC and by month for 2016

- finaldataframecopy_wWeather.csv includes all data available
- Sample_Size_1661.csv includes a balanced dataset, of 1661 for each class, this was the data that was used for the final machine learning

**EDA: **
This folder contains charts that examine the characteristics of Naracan recepients and the types of calls

**Models: **
The models folder contains all of the machine learning that was done with all data sets and all features until we were able to figure out the perfect predicting issues. 
The Final Models folder contains the machine learning that was used in the analysis once we figure out why our models weren't working properly.  