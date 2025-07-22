# House Price Prediction Model
This repository contains a project that predicts house prices based on various features using a machine learning model. The model is implemented in a Jupyter notebook (`main.ipynb`) and `main.py`, and the repository is set up with continuous integration using Jenkins.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Jenkins Pipeline](#jenkins-pipeline)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project is part of my college coursework. It utilizes a machine learning model to predict house prices based on a dataset of features like number of bedrooms, square footage, location, etc.

The main goals of the project are:
- Data preprocessing and cleaning.
- Building and training a regression model.
- Evaluating model performance.
- Automating the project with a Jenkins pipeline for continuous integration.

## Features
- **Machine Learning Model**: A Jupyter notebook that contains data preprocessing, model training, and evaluation.
- **Jenkins Pipeline**: The pipeline automates fetching the code from GitHub, building the model, and running tests.
- **Data Visualization**: Includes charts and plots to analyze the dataset.

## Installation

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Jupyter Notebook
- Required Python libraries (`requirements.txt`)

To install dependencies, run:

```bash
pip install -r requirements.txt
```
## Running the Jupyter Notebook

To explore the model or retrain it, open main.ipynb using Jupyter Notebook:

```bash
jupyter notebook main.ipynb
```
## Usage

1. Clone the repository:

```bash
    git clone https://github.com/ShrijithSM/House-Price-Prediction.git
```
2. Install the required dependencies.
3. Run the Jupyter notebook (main.ipynb) to train or evaluate the model.

## Jenkins Pipeline

This project is integrated with Jenkins for continuous integration (CI). The Jenkins pipeline defined in the Jenkinsfile automates the following stages:

1. Checkout: Pulls the latest code from the repository.
2. Build: Runs the model training script (python_file.py).
3. Test: Verifies that the training and model operations were successful.

## Setting Up Jenkins

1. Install Jenkins on your server.
2. Configure Git and Python on the Jenkins machine.
3. Set up the credentials (credentialsId) to access the GitHub repository.
4. Create a new pipeline job in Jenkins and configure it to use the Jenkinsfile in this repository.

## Model Training

The machine learning model is built using the following steps:

1. Data Preprocessing: Cleans the data, handles missing values, and performs feature scaling.
2. Model Building: A regression model is trained on the dataset.
3. Evaluation: The model is evaluated using metrics like Mean Squared Error (MSE) and R-squared.

The model is implemented in the `main.ipynb` notebook.

## Contributing

If you'd like to contribute to this project, feel free to open a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
