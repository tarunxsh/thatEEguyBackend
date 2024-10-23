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