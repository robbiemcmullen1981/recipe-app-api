# recipe-app-api

recipe app api source code

1. To get the docker image in the command line: docker build .
2. To run container: docker-compose run app sh -c "django-admin.py startproject app ."
3. got to travis-ci.org, sign in with github and sync projects then toggle on recipe app
4. to run tests: docker-compose run app sh -c "python manage.py test"
5. for linting: docker-compose run app sh -c "python manage.py test && flake8"
6. useful command: docker-compose run app sh -c "python manage.py startapp core"
