# NLP Project

This repository contains the code and configurations for the NLP project for COMM061 coursework.


## Using the CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration and Continuous Deployment (CI/CD). The pipeline is configured to automatically build, test, and deploy the application whenever changes are pushed to the `main` branch or a pull request is made to the `main` branch.

### How to Use the CI/CD Pipeline

1. **Triggering the Pipeline**:
   - **Push to Main Branch**: Any code pushed to the `main` branch will trigger the pipeline.
   - **Pull Request**: Any pull request made to the `main` branch will also trigger the pipeline.

2. **Pipeline Jobs**:
   - **Build Job**: Runs on `windows-latest`.
     - **Steps**:
       1. **Checkout Code**: The code is checked out from the repository.
       2. **Set Up Python**: Python 3.8 is set up.
       3. **Install Dependencies**: Dependencies are installed from `requirements.txt`.
       4. **Test the Application**: Tests are executed using `pytest`.
   - **Deploy Job**: Runs on `windows-latest`.
     - **Steps**:
       1. **Checkout Code**: The code is checked out from the repository.
       2. **Set Up Python**: Python 3.8 is set up.
       3. **Install Dependencies**: Dependencies are installed from `requirements.txt`.
       4. **Deploy the Application**: The Flask application is deployed using `nohup flask run --host=0.0.0.0 &`.

3. **Configuration File**:
   - The CI/CD pipeline is configured using the YAML file located at `.github/workflows/ci_cd_pipeline.yml`.

### Running the Pipeline Locally

To run the pipeline or individual steps locally, follow these commands:

1. **Set Up Python Environment**:
   ```sh
   python -m pip install --upgrade pip
   pip install -r requirements.txt

**Run Tests**:

python -m pytest tests/

**Run Application**:
flask run --host=0.0.0.0

Adding New Tests
Create Test Files: Add your test cases in the tests directory.
Ensure Imports: Adjust the Python path in your test files if needed.
Run Tests: Use pytest to run your tests locally.

