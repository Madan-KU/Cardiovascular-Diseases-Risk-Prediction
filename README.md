
# Cardio Vascular Prediction Tool

This tool leverages machine learning to predict the likelihood of cardiovascular diseases. It's designed to be containerized and deployable, ensuring ease of use and scalability.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Model](#model)
6. [Deployment](#deployment)
7. [Screenshots](#screenshots)
8. [Contribution](#contribution)

## Features

- Predictive modeling of cardiovascular diseases.
- Docker support for containerization.
- AWS Elastic Beanstalk and Heroku configurations for easy deployment.
- Comprehensive data exploration and preprocessing notebooks.

## Installation

**Prerequisites**:
- Docker (if you want to use the containerized version)
- Python 3.x

**Steps**:

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Local Execution

1. Run the application:
   ```bash
   python application.py
   ```

### Docker

1. Build the Docker image:
   ```bash
   docker build -t cvp_tool .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 cvp_tool
   ```

## Data

The `data` directory contains the datasets utilized in this project. Ensure to follow ethical considerations when using and sharing this data.

## Model

Trained models are stored in the `models` directory. The Jupyter notebooks in the `notebooks` directory provide detailed insights into data preprocessing, exploration, and model training.

## Deployment

### Heroku

The project is live on Heroku: [Cardio Vascular Prediction Tool on Heroku](https://cardio-vascular-diseases-77bacdb4950a.herokuapp.com/)

### AWS Elastic Beanstalk

The project is configured for deployment on AWS Elastic Beanstalk. However, the Elastic Beanstalk deployment is currently not active, and there is no live URL available at this time.

## Screenshots

Visual demonstrations and application snapshots are available in the `Screenshots` directory.

## Contribution

Contributions are welcome! Please fork the repository and create a pull request with your changes.
