import os

from fastapi import FastAPI


APP_NAME = "CloudLatch"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "development")

app = FastAPI(
    title=APP_NAME,
    description="Containerised service for demonstrating cloud deployment and DevOps workflows.",
    version=APP_VERSION,
)


@app.get("/")
def root():
    return {
        "service": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENVIRONMENT,
        "message": "CloudLatch is running.",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/ready")
def readiness():
    return {
        "status": "ready",
        "service": APP_NAME,
    }


@app.get("/version")
def version():
    return {
        "service": APP_NAME,
        "version": APP_VERSION,
    }