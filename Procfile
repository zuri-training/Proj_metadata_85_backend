release: python src/manage.py migrate
web: gunicorn xtracto.wsgi --log-file -
web: python src/manage.py runserver 0.0.0.0:$PORT