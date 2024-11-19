# ci-cd-jenkins-selenium-pytest
# CI/CD with Jenkins, Selenium, and Pytest

    /ci-cd-jenkins-selenium-pytest
    │
    ├── /config
    │   ├── test.yaml
    │   ├── staging.yaml
    │   └── production.yaml
    ├── /tests
    │   ├── /test_login.py
    │   └── /test_registration.py
    ├── conftest.py
    ├── requirements.txt
    ├── Jenkinsfile  # New file added for Jenkins configuration
    └── README.md

## Pipeline Overview

### Stages

1. **Checkout SCM**  
   - Retrieves the latest code from the Git repository.

2. **Set up Python Environment**  
   - Creates a Python virtual environment using Python 3.8.
   - Installs the required dependencies listed in `requirements.txt`.

3. **Run Tests**  
   - Executes tests using `pytest`.
   - If tests fail, it marks the stage as a failure but allows the pipeline to continue.

4. **Upload Test Report**  
   - Optionally upload or store the test report (customizable for your needs).

5. **Post Actions**  
   - Includes optional steps for actions such as cleanup or notifications.

### Post Actions

- The pipeline performs cleanup actions, like removing temporary files or virtual environments, after every build.
- It also logs a success or failure message depending on the result of the tests.

## Requirements

- Python 3.8 (configured in the pipeline)
- `requirements.txt` file with the necessary dependencies for your project.
- Jenkins with pipeline support.

## How to Use

1. Ensure you have Jenkins set up with pipeline support.
2. Create a new pipeline job in Jenkins and point it to your repository.
3. Configure the pipeline to use the Jenkinsfile (found in this repository).
4. Run the pipeline, and it will automatically handle setting up the environment and running tests.