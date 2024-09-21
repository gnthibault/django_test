# Django tests

## Project creation
```bash
brew install poetry
pyenv install -v 3.12.5
poetry env use python3.12 # creates virtualenv
poetry new django_test --name django_test
cd django_test
git init
git remote add origin git@github.com:gnthibault/django_test.git
git add .
git commit -am "first commit"
git push --set-upstream origin main
```

Add new dependencies
```bash
poetry add django
poetry add django-debug-toolbar
poetry run django-admin startproject django_app . # Creates whole project
```

Run server

```bash
poetry run python manage.py runserver # Runs ...
poetry run python manage.py startapp playground # Adds a subdirectory with preconfigured set of files for this module
# Think about adding the INSTALLED_APPS from your main appl directory settings.py
poetry run python manage.py makemigrations # creates migrations files, for instance when models are changed
poetry run python manage.py sqlmigrate your_app_name 004 # generates SQL code for you migration id 004 and shows it just to check
poetry run python manage.py migrate # Actually apply the migrations generated at the makemigrations step
```
## Project checkout


```bash
git clone git@github.com:gnthibault/django_test.git
cf django_test
deactivate
poetry install
```
