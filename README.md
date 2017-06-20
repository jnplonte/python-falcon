# FALCON BOILERPLATE
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()
[![Build Status](https://travis-ci.org/jnplonte/python-falcon.svg?branch=master)](https://travis-ci.org/jnplonte/python-falcon)


## Dependencies
* python: [https://www.python.org/](https://www.python.org/)
* falconframework: [https://falconframework.org/](https://falconframework.org/)
* pip: [https://pypi.python.org/pypi/pip](https://pypi.python.org/pypi/pip)
* uwsgi: [http://uwsgi-docs.readthedocs.io/](http://uwsgi-docs.readthedocs.io/en/latest/)
* nose: [http://nose.readthedocs.io/](http://nose.readthedocs.io/en/latest/)


## Installation
- create virtualenv `virtualenv my_project`
- work on virtualenv `workon my_project`
- install python dependencies by running `pip install`

## How to Use
- run `uwsgi run.ini` it will listen to default http://localhost:8282


## Testing
- run `nosetests -v`


## Building Production
- run `uwsgi run.ini --set env=prod`
