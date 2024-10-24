#!/usr/bin/env bash

# Whenever you deploy a new version of your project, Render runs a build command to prepare it for production.
# This executable script for Render to run as this build command.

# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
# pip install -r requirements.txt
pip install poetry
poetry install

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# create super user on first deploy
# Set the env var CREATE_SUPERUSER, deploy to have the command run,
if [[ -z $CREATE_SUPERUSER ]]; then poetry run python manage.py createsuperuser --no-input; fi
# then remove the CREATE_SUPERUSER env var, so it’s not run again.