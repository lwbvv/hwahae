web: gunicorn myapp.wsgi --log-file -
migrate: python manage.py migrate --settings=myapp.settings.production
seed: python manage.py loaddata myapp/item/fixtures/items-product.json
seed: python manage.py loaddata myapp/item/fixtures/items-ingredient.json
