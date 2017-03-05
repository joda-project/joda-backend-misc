# Building joda-backend-misc for development

Joda backend packages are powered by Python and Django.

## Requirements
You will need the following things properly installed on your computer:
* [Git](https://git-scm.com)
* [Python 3](https://python.org) with pip
* [Foreman](https://ddollar.github.io/foreman/) (optional)

## Installation
* Install [joda-backend](https://github.com/joda-project/joda-backend/blob/master/BUILDING.md)
* `git clone https://github.com/joda-project/joda-backend-misc` this repository
* `cd joda-backend-misc`

## Running Tests
Symlink `joda` and `joda_core` folders from main backend.
Run `coverage run runtests.py`. To see coverage report run `coverage report`.
