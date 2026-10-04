"""
config.py
=========
Application configuration settings loaded from environment variables.
"""

import os
from dotenv import load_dotenv

# Base directory of the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Load variables from .env if present
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-dev-secret-key-change-me")
    DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"
    PORT = int(os.environ.get("PORT", 5000))
    
    # Machine Learning artifact paths
    ML_DIR = os.path.join(BASE_DIR, "ml")
    SAVED_MODELS_DIR = os.path.join(ML_DIR, "saved_models")
    MODEL_PATH = os.path.join(SAVED_MODELS_DIR, "model.joblib")
    METRICS_PATH = os.path.join(SAVED_MODELS_DIR, "metrics.json")
    CONFIG_PATH = os.path.join(SAVED_MODELS_DIR, "preprocessing_config.json")
    
    # Maximum allowed payload size (2MB)
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
