# CloudLatch

CloudLatch is a containerised FastAPI service built to explore practical DevOps workflows including automated testing, CI/CD, container publishing and Infrastructure as Code.

The application is intentionally lightweight, allowing the project to focus on how software is tested, packaged, configured and provisioned through a repeatable delivery workflow.

## Tech Stack

**Application:** Python, FastAPI, Uvicorn, Pytest  
**DevOps:** Docker, Docker Compose, GitHub Actions, GitHub Container Registry  
**Infrastructure:** Terraform, LocalStack, AWS CLI, Amazon S3, Amazon SQS

## Architecture

```text
                    GitHub
                      |
               GitHub Actions
                 /         \
              Tests      Docker Build
                             |
                             v
                            GHCR

Local Development
      |
      +---- Docker Compose ---- CloudLatch API
      |
      +---- LocalStack -------- AWS Emulation
                                  |
                              Terraform
                              /       \
                            S3         SQS
```

## Features

- FastAPI service with health and readiness endpoints
- Runtime configuration through environment variables
- Automated API tests with Pytest
- Containerisation with Docker
- Container health checks
- Local orchestration with Docker Compose
- CI pipeline with GitHub Actions
- Automated Docker image publishing to GHCR
- AWS service emulation using LocalStack
- Infrastructure provisioning with Terraform
- Terraform-managed S3 bucket and SQS queue

## API

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Service information |
| `GET` | `/health` | Health check |
| `GET` | `/ready` | Readiness check |
| `GET` | `/version` | Application version |

## CI/CD

CloudLatch uses GitHub Actions to automate the build pipeline.

On pushes and pull requests to `main`, the workflow:

1. installs project dependencies;
2. runs the Pytest test suite;
3. builds the Docker image;
4. publishes successful images to GitHub Container Registry.

Published images are tagged with `latest` and the corresponding Git commit SHA.

## Infrastructure as Code

Terraform is used to define the supporting infrastructure for CloudLatch.

For development, AWS services are emulated locally with LocalStack rather than provisioned in a real AWS account.

Terraform currently provisions:

```text
S3
└── cloudlatch-local-storage

SQS
└── cloudlatch-events
```

The infrastructure was verified through the AWS CLI, and subsequent Terraform plans return no changes when the deployed resources match the configuration.

> LocalStack is used for local AWS emulation. This project does not represent a production deployment to AWS.

## Running Locally

### Application

Create a virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the tests:

```bash
pytest -v
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The API is available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

### Docker Compose

Build and start the container:

```bash
docker compose up --build -d
```

Check its health:

```bash
docker compose ps
```

Stop the container:

```bash
docker compose down
```

## Local Infrastructure

Start LocalStack:

```bash
lstk start
```

Initialise Terraform:

```bash
cd terraform
terraform init
terraform validate
```

Preview the infrastructure:

```bash
lstk terraform plan
```

Provision it:

```bash
lstk terraform apply
```

Verify the resources:

```bash
aws --profile localstack s3api list-buckets
aws --profile localstack sqs list-queues
```

## Project Structure

```text
CloudLatch/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   └── main.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── .dockerignore
├── .gitignore
├── compose.yml
├── Dockerfile
├── LICENSE
├── README.md
└── requirements.txt
```

## What I Learned

Building CloudLatch gave me hands-on experience with:

- creating and testing containerised services;
- designing CI workflows around automated tests and Docker builds;
- publishing versioned container images;
- configuring applications through runtime environment variables;
- defining infrastructure using Terraform;
- working with AWS-style S3 and SQS APIs in a local environment;
- troubleshooting interactions between Docker, Terraform, LocalStack and AWS tooling.

## Future Improvements

- Deploy the container to a managed cloud platform
- Add container vulnerability scanning
- Add Terraform security scanning to CI
- Introduce application metrics and observability
- Use remote Terraform state for a deployed environment

## Documentation

A detailed technical report covering the system architecture, containerisation, CI/CD pipeline, Infrastructure as Code, LocalStack environment, testing and development challenges is available below.

[View the CloudLatch Technical Report](docs/CloudLatch-Technical-Report.pdf)

## License

MIT License
