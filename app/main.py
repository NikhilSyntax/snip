import logging

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.core.config import settings

# Create a logger for this module.
logger = logging.getLogger(__name__)

# Create the FastAPI application.
app = FastAPI(
    title=settings.app_name
)


# -----------------------------------------
# 1. HEALTH CHECK ENDPOINT
# -----------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "snip-api",
    }

@app.get("/docs/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=f"{settings.app_name} API Documentation",
    )