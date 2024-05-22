#NLP Project

This repository contains the code and configurations for the NLP project for COMM061 coursework.

## Project Summary

This project focuses on building and deploying an NLP (Natural Language Processing) model for sequence classification to detect abbreviations and long forms. The following steps were taken to achieve this:

1. **Data Analysis and Visualization**:
   - Loaded the dataset and conducted exploratory data analysis to understand the data distribution.
   - Visualized the frequency of different NER tags and token counts.

2. **Model Training**:
   - Utilized a pre-trained RoBERTa model fine-tuned for NER (Named Entity Recognition).
   - Implemented functions to load the model and make predictions.

3. **Web Application**:
   - Developed a Flask web application to serve the model.
   - The application accepts input text from users, processes it using the model, and returns predictions.

4. **CI/CD Pipeline**:
   - Implemented a CI/CD pipeline using GitHub Actions to automate building, testing, and deploying the model.
   - The pipeline ensures that any changes to the code or data are automatically integrated and deployed, maintaining a consistent and up-to-date deployment.

## CI/CD Pipeline Setup

In this project, we set up a CI/CD (Continuous Integration and Continuous Deployment) pipeline using GitHub Actions. This pipeline automates the process of building, testing, and deploying our NLP model. Below is a detailed explanation of the steps and configurations involved:

1. **Repository Creation and Structure**:
   - Created a GitHub repository named `my-nlp-project`.
   - Structured the repository with necessary directories and files, including `app`, `model`, and `.github/workflows`.

2. **Directory and File Setup**:
   - **app/main.py**: Contains the Flask web server setup to handle requests and interact with the model for predictions.
   - **app/roberta.py**: Contains functions to load the pre-trained RoBERTa model and make predictions.
   - **requirements.txt**: Lists the project dependencies (`Flask`, `transformers`, and `torch`).
   - **.github/workflows/ci_cd_pipeline.yml**: Defines the GitHub Actions workflow for CI/CD.

3. **GitHub Actions Workflow**:
   - **Triggers**: The workflow is triggered on pushes and pull requests to the `main` branch.
   - **Build Job**:
     - Checks out the code.
     - Sets up Python environment.
     - Installs dependencies.
     - Runs tests (placeholder for actual test commands).
   - **Deploy Job**:
     - Depends on the build job.
     - Checks out the code.
     - Sets up Python environment.
     - Installs dependencies.
     - Deploys the Flask application, making it accessible via an HTTP endpoint.

4. **Commit and Push**:
   - Added and committed all files to the repository.
   - Pushed the changes to the `main` branch, triggering the CI/CD pipeline.
