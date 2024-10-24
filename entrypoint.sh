#!/usr/bin/env bash

# This the entrypoint script for web container.
# These run on container start

# Exit on error
set -o errexit

# Convert static asset files
poetry run python manage.py collectstatic --no-input

# Apply any outstanding database migrations
poetry run python manage.py migrate

# create super user on first deploy
# Set the env var CREATE_SUPERUSER, deploy to have the command run,
if [[ -z $CREATE_SUPERUSER ]]; then poetry run python manage.py createsuperuser --no-input; fi
# then remove the CREATE_SUPERUSER env var, so it’s not run again.


# run the server
poetry run python -m gunicorn blogger.wsgi --bind 0.0.0.0:8000