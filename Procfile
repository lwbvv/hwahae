web: gunicorn myapp.wsgi --log-file -
makemigrations: python manage.py makemigrations --settings=myapp.settings.production
migrate: python manage.py migrate --settings=myapp.settings.production
seed: python manage.py loaddata myapp/item/fixtures/indredient-data.json
seed: python manage.py loaddata myapp/item/fixtures/product-data.json
