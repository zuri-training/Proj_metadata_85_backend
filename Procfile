release: python src/manage.py makemigrations
release: python src/manage.py migrate
release: python manage.py migrate auth
release: python manage.py migrate --run-syncdb
release: python src/manage.py migrate
release: python src/manage.py runserver 0.0.0.0:$PORT
web: gunicorn xtracto.wsgi --log-file -



