#!/bin/bash

echo "Migrating database"
python manage.py migrate

# echo "Collecting static variables"
# python manage.py collectstatic

echo "Loading fixtures"
python manage.py loaddata */fixtures/*.yaml

echo "Creating dev admin"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'pass')" | python manage.py shell

echo "Running server"
python manage.py runserver 0.0.0.0:8000