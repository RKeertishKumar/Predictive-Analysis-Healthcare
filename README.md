# Predictive-Analysis-Healthcare
Revolutionize healthcare resource allocation with predictive analysis, leveraging telemedicine to efficiently address the pressing needs of underserved regions.
## Table of Contents
- [Project Overview](#overview)
- [Project Inspiration](#inspiration)
- [Project Objectives](#what-it-does)
- [Technical Stack](#tech-stack)
- [Challenges Encountered](#challenges-faced)
- [Repository Information](#repository-name)
- [Elevator Pitch](#elevator-pitch)
- [Technical Implementation](#how-its-built)
- [Setup and Dependencies](#setup)
- [Data Preprocessing](#data-preprocessing)
- [Data Visualization](#data-visualization)
- [Random Forest Predictive Analysis](#random-forest-predictive-analysis)
- [Analysis Results](#analysis-results)



## Overview
The project addresses the critical issue of stress among medical doctors and its implications for the healthcare industry. It aims to predict and analyze stress levels, provide insights, and offer scalable models for healthcare systems.

## Setup
```shell
pip install -r requirements.txt
```
To download all the dependencies

## Inspiration
The doctors and interns around me seemed to have a hectic life with bad work life balance often due to high workload. I believed that proper allocation of resources would lessen their burden and would allow them to give better quality of service. And hence this project.

## What It Does
Collect and analyze data related to stress levels among medical doctors. Identify the prevalence and patterns of stress and its associated risk factors. Develop predictive models to determine the likelihood of doctors experiencing stress. Provide actionable insights to healthcare systems for resource allocation and interventions. Incorporate location data to offer a more comprehensive view, from countries to states. Ultimately, the project seeks to reduce stress among medical doctors, improve healthcare quality, and enhance the overall well-being of healthcare professionals.

## To run the code for predictive analysis using random forest
```shell
python ml_ran_for.py
```

## Analysis after using Random Forest
![image](https://github.com/RKeertishKumar/Predictive-Stress-Analysis-Healthcare/assets/141417594/81c7139b-107f-44b2-bca2-7119383bea44)

## Data Preprocessing
```shell
python prepro.py
```
Which does the hot encoding and scaling and fixing null values.

## Data Visualization
Available in the images folder.
To run it again, 
```shell
python Datavis.py
```
## Tech Stack
- **Python**
- Libraries and Frameworks: pandas, Matplotlib, Seaborn, Scikit-Learn, Random Forest
- **Excel** for data manipulation
- **Machine Learning**: Random Forest

## Challenges Faced
- Data Quality
- Data Exploration
- Feature Engineering
- Machine Learning
- Data Privacy
- Scalability
- Resource Allocation
- Interdisciplinary Collaboration

## Repository Name
- **Repository Name**: Predictive-Analysis-Healthcare

## Project Elevator Pitch
In a world where medical doctors face unprecedented levels of stress, our project uses data-driven techniques to comprehensively understand stress and its associated risk factors. It provides actionable insights to enhance the quality of healthcare and the well-being of medical professionals.

## How It's Built
- **Python**: The core programming language for data analysis and machine learning.
- **Libraries and Frameworks**: pandas, Matplotlib, Seaborn, Scikit-Learn, and Random Forest for data manipulation, visualization, analysis, and machine learning.
- **Excel**: Used for data manipulation and initial data exploration.
- **Machine Learning**: Random Forest was applied to create a predictive model.

