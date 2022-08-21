web: gunicorn xtracto.wsgi --log-file -
release: python src/manage.py makemigrations
release: python src/manage.py migrate
web: python src/manage.py runserver 0.0.0.0:$PORT