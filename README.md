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
```

## Project checkout


```bash
git clone git@github.com:gnthibault/django_test.git
cf django_test
poetry install
```
