#!/usr/bin/env bash
# exit on error
set -o errexit


# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

if [[ $CREATE_SUPERUSER ]];
then
    python manage.py createsuperuser --no-input --username "$SUPERUSER_USERNAME" --email "$SUPERUSER_EMAIL"
fi
