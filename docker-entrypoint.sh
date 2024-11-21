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
# Create superuser with predefined credentials
echo "Creating superuser"
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@email.com', 'admin')
EOF

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000