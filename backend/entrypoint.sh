#!/bin/bash

echo "Migrating database"
python3 manage.py migrate

# echo "Collecting static variables"
# python manage.py collectstatic

echo "Loading fixtures"
python3 manage.py loaddata bikeproperties/fixtures/*.yaml -i
python3 manage.py loaddata bikeparts/fixtures/*.yaml -i

echo "Creating dev admin"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'pass')" | python3 manage.py shell

echo "Running server"
python3 manage.py runserver 0.0.0.0:8000