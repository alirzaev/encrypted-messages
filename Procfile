release: python manage.py migrate
web: gunicorn -b 0.0.0.0:$PORT project.wsgi:application