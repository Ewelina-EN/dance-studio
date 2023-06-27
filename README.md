# django-w-godzine
Projekt to webinaru  "Django w godzinę" przeprowadzonego w ramach [akakademiait.com.pl](https://akakademiait.com.pl)
Komendy:
PIPENV_VENV_IN_PROJECT=1   pipenv install
pipenv install django
pipenv shell
django-admin startproject django_in_one_hour
python manage.py startapp notes
python manage.py makemigrations
python manage.py migrate

https://tinyurl.com/django-ankieta

# Aktualizacja strony

git pull
pipenv install
./manage.py migrate
./manage.py createsuperuser # to tworrzy admina, zada pytania. Haslo jest generalnie dowolne, nie musi byc silne, bo tylko lokalnie.
./manage.py runserver

Dokumentacja templatów:
https://docs.djangoproject.com/en/4.2/ref/templates/language/