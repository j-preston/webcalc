# webcalc
Project Structure
Frontend (Flask App)

A simple web interface for the calculator.
Users can enter numbers and select operations (add, subtract, multiply, divide).
Communicates with the FastAPI backend to perform calculations.
Backend (FastAPI Service)

An API that performs the actual calculations.
Endpoints for different operations (add, subtract, multiply, divide).
Returns the result of the calculation to the frontend.
CI/CD Pipeline Steps
Development with VS Code

Use VS Code for writing and testing your code.
Utilize extensions for Python, Flask, and FastAPI for better productivity.
Version Control with GitHub

Push your code to a GitHub repository.
Utilize branches for feature development and bug fixes.
Continuous Integration with Jenkins

Set up Jenkins to watch your GitHub repository.
On each push, Jenkins pulls the latest code.
Build Phase: Jenkins runs a build process, which might include setting up virtual environments, installing dependencies, etc.
Test Phase: Jenkins executes automated tests. For the frontend, this could include UI tests; for the backend, unit tests for each operation.
Report Phase: Generate test reports for later review.
Continuous Deployment with Jenkins

Upon successful integration (passing all tests), Jenkins can deploy the application to a staging or production environment.
This could involve deploying the Flask app and FastAPI service to cloud services or an in-house server.
Additional CI/CD Features
Docker Integration: Containerize both Flask and FastAPI applications for consistent deployment environments.
Database Integration: If you decide to store calculation logs or user data, demonstrate handling database migrations in the pipeline.
Performance Testing: Include performance testing in the Jenkins pipeline to ensure that the application performs well under load.
Security Scanning: Implement code security scanning tools in the pipeline for automatic vulnerability checks.
Learning and Demonstration Opportunities
Show how changes in the frontend or backend trigger the CI pipeline.
Demonstrate handling merge conflicts and feature branch strategies.
Showcase how CI/CD can catch bugs early through automated testing.
Explain the importance of different environments (development, staging, production) in the deployment process.

Making a change to the readme