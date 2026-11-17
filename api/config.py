# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import secrets
import sys

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Do not override variables already set in the environment.
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))


def resolve_secret_key():
    """Return the Flask secret key from the environment.

    Development may start with an ephemeral key so a local run does not
    depend on a committed secret. Every other environment must set SECRET_KEY.
    """
    configured = os.environ.get("SECRET_KEY", "").strip()
    if configured:
        return configured

    flask_env = os.environ.get("FLASK_ENV", "").strip().lower()
    if flask_env == "development":
        print(
            "WARNING: SECRET_KEY is not set. Using an ephemeral key because "
            "FLASK_ENV=development. Sessions will not survive a restart. "
            "Set SECRET_KEY in the environment for a stable key (see .env.example).",
            file=sys.stderr,
        )
        return secrets.token_urlsafe(32)

    raise RuntimeError(
        "SECRET_KEY is not set. Copy .env.example to .env and set SECRET_KEY, "
        "or export SECRET_KEY before starting the app. Startup refuses to "
        "continue outside FLASK_ENV=development without a secret key."
    )


class BaseConfig():

    SQLALCHEMY_DATABASE_URI        = 'sqlite:///' + os.path.join(BASE_DIR, 'apidata.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = resolve_secret_key()
