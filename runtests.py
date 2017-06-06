#!/usr/bin/env python
import sys
from os.path import dirname, abspath

import django
from django.conf import settings
from django.core.management import execute_from_command_line


# Give feedback on used versions
sys.stderr.write('Using Python version {0} from {1}\n'.format(
    sys.version[:5], sys.executable))
sys.stderr.write('Using Django version {0} from {1}\n'.format(django.get_version(),
                                                              dirname(abspath(django.__file__))))

if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:'
            }
        },
        TEST_RUNNER='django.test.runner.DiscoverRunner',
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.messages',
            'django.contrib.sites',
            'django.contrib.admin',
            'joda_core',
            'joda_misc',
        ),
        MIDDLEWARE_CLASSES=(),
        AUTH_USER_MODEL='joda_core.User'
    )

DEFAULT_TEST_APPS = [
    'joda_misc',
]


def runtests():
    other_args = list(filter(lambda arg: arg.startswith('-'), sys.argv[1:]))
    test_apps = list(filter(lambda arg: not arg.startswith(
        '-'), sys.argv[1:])) or DEFAULT_TEST_APPS
    argv = sys.argv[:1] + ['test', '--traceback'] + other_args + test_apps
    execute_from_command_line(argv)

if __name__ == '__main__':
    runtests()
