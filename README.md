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
poetry run django-admin startproject django_app .
```

Run server

```bash
poetry run python manage.py runserver
poetry run python manage.py startapp playground
```
## Project checkout


```bash
git clone git@github.com:gnthibault/django_test.git
cf django_test
deactivate
poetry install
```
