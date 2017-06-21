# FALCON BOILERPLATE
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()
[![Build Status](https://travis-ci.org/jnplonte/python-falcon.svg?branch=master)](https://travis-ci.org/jnplonte/python-falcon)


## Dependencies
* python: [https://www.python.org/](https://www.python.org/)
* mysql: [https://www.mysql.com/](https://www.mysql.com/)
* falconframework: [https://falconframework.org/](https://falconframework.org/)
* pip: [https://pypi.python.org/pypi/pip](https://pypi.python.org/pypi/pip)


## Installation
- create virtualenv `virtualenv my_project`
- work on virtualenv `workon my_project`
- install python dependencies by running `pip install`
- create database and update database settings on `{root}\app\config.py`
- run database migration `python _migrate.py`


## How to Use
- run `uwsgi run.ini` it will listen to default http://localhost:8282


## Testing
- run `nosetests -v`


## Building Production
- run `uwsgi run.ini --set env=prod`
