joda-backend-misc
=====================
Miscellaneous documents support for Joda - Backend

Quick start
-----------
1. Install package ``pip install joda_misc`` inside Joda virtual environment.

2. Add Joda Misc to your ``INSTALLED_APPS`` and ``JODA_FEATURES`` settings::

    INSTALLED_APPS = [
        ...
        'joda_misc',
    ]

    JODA_FEATURES = [
        ...
        'misc',
    ]

3. Run ``python manage.py migrate`` to create the misc content models.


Copyright info
--------------
Copyright (C) 2016-2017 Tadej Novak

This project may be used under the terms of the
GNU Affero General Public License version 3.0 as published by the
Free Software Foundation and appearing in the file LICENSE.md.
