#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
#dummy data
echo "Dummy data"
python manage.py seed_db
#collect static
echo "Collect static"
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000