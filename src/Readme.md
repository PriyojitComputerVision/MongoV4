# Data Engineering and Machine Learning Pipeline

This repository contains a data engineering and machine learning pipeline that involves data cleaning, model training, MongoDB storage, model evaluation, and Docker containerization.

## Table of Contents
- [Introduction](#introduction)
- [Data Cleaning](#data-cleaning)
- [Model Training](#model-training)
- [MongoDB Storage](#mongodb-storage)
- [Model Evaluation](#model-evaluation)
- [Docker Containerization](#docker-containerization)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases a complete pipeline for data engineering and machine learning tasks. It covers data cleaning, training a machine learning model, storing data in MongoDB, evaluating the model, and containerizing the solution using Docker.

## Data Cleaning

Explain how data cleaning is performed using MongoDB:
- Load raw data into MongoDB collections.
- Apply necessary data cleaning operations.
- Store cleaned data in MongoDB.

## Model Training

Detail the model training process:
- Select features and target variable.
- Split data into training and testing sets.
- Train machine learning models (Linear Regression, XGBoost, etc.).
- Choose the best model based on cross-validation.

## MongoDB Storage

Explain how data is stored in MongoDB:
- Store cleaned data in separate MongoDB collections.
- Describe the data schema and structure used in MongoDB.

## Model Evaluation

Describe the model evaluation process:
- Evaluate the best model using appropriate metrics (MSE, MAE, R2).
- Compare model performance against different evaluation criteria.

## Docker Containerization

Explain Docker containerization of the pipeline:
- Include necessary dependencies and configurations.
- Build a Docker image and run containers for the solution.

## Usage

Provide steps to run the pipeline and Docker container:
1. Clone the repository:

2. Install required dependencies:

3. Run the data cleaning and model training scripts:

4. Store data in MongoDB:
- Ensure MongoDB is running and accessible.
- Run the MongoDB storage script:
  ```
  python data_ingestion.py
  ```
5. Evaluate the model:

6. Docker containerization:
- Build Docker image:
  ```
  docker build -t your-image-name .
  ```
- Run Docker container:
  ```
  docker run -it your-image-name
  ```


## License

This project is licensed under the [MIT License](LICENSE).

