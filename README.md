[![flake8 Lint](https://github.com/acdh-oeaw/freud_api_crawler/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/freud_api_crawler/actions/workflows/lint.yml) [![codecov](https://codecov.io/gh/acdh-oeaw/freud_api_crawler/branch/master/graph/badge.svg?token=7OBAOGEFTY)](https://codecov.io/gh/acdh-oeaw/freud_api_crawler)

# Freud API Crawler

A client to interact with freud-net API


## install

* create a virtual environment and install the package with `pip install freud_api_crawler` 
* provide FRD_USER (freud-net username) and FRD_PW (freud-net password) as environment varibles, e.g. by
  * create a file called `env.secret` to store you freud-net api credentials
  * run `./set_env_variables.sh` 

### example `env.secret`

```
FRD_USER=username
FRD_PW=password
```

## dev

* clone the repo
* create virtual env
* install dev-depenencies `pip install -r requirements_dev.txt`
* install the package (so you have the actual dependencies as well) `pip install -e .`

* run test with `coverage run -m pytest -v`
* create test-report `coverage report` or `coverage html`

## api-utils

### get work by title

https://www.freud-edition.net/jsonapi/node/werk?filter[field_titel.value]=%C3%9Cber%20den%20Traum
https://www.freud-edition.net/jsonapi/node/werk?filter[field_titel.value]=Über den Traum

### get manifestaion by node id

this ID can be taken from edit-url, e.g. https://www.freud-edition.net/node/51190/edit

https://www.freud-edition.net/jsonapi/node/manifestation?filter[drupal_internal__nid]=51190
