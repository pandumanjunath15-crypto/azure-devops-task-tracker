# Azure DevOps Task Tracker

A small Python Flask REST API designed as a starter project for learning Azure DevOps CI pipelines.

## Features

- List, create, update, and delete tasks
- Health-check endpoint
- Unit tests using Python's built-in `unittest`
- Azure Pipelines YAML for CI on `main` and `develop`
- ZIP build artifact published by the pipeline
- Dockerfile for container-based local runs

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

The API listens on `http://localhost:5000`.

## API examples

```bash
curl http://localhost:5000/health
curl http://localhost:5000/api/tasks

curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Learn Azure Boards"}'

curl -X PATCH http://localhost:5000/api/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed":true}'

curl -X DELETE http://localhost:5000/api/tasks/1
```

## Run tests

```bash
pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
```

## Run with Docker

```bash
docker build -t azure-devops-task-tracker .
docker run --rm -p 5000:5000 azure-devops-task-tracker
```

## Set up Azure DevOps

1. Create an Azure DevOps organization and project.
2. Create a Git repository in the project.
3. Push this folder's contents to the repository.
4. In Azure DevOps, open **Pipelines > New pipeline**.
5. Select your repository and choose **Existing Azure Pipelines YAML file**.
6. Select `/azure-pipelines.yml`, review it, and run the pipeline.
7. Open the successful run and download the `drop` artifact.

The pipeline selects Python 3.12, installs dependencies, runs unit tests, packages the application, and publishes the ZIP as a build artifact.

## Suggested project extensions

- Add Azure Boards work items and sprint planning.
- Add branch policies requiring a passing build.
- Add code coverage and static analysis.
- Add a deployment stage targeting Azure App Service or Azure Container Apps.
- Store deployment secrets in a variable group backed by Azure Key Vault.

## Notes

This is a learning starter, not a production service. It uses in-memory task storage, so tasks reset when the process restarts. Add persistent storage, authentication, input limits, and production server configuration before deploying real workloads.
