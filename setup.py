import os
from setuptools import find_packages, setup

import joda_misc

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()


def get_version(version):
    """Return a PEP 440-compliant version number from VERSION."""
    main = '.'.join(str(x) for x in version[:3])
    sub = ''

    if version[3] != 'final' and version[4] != 0:
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'rc'}
        sub = mapping[version[3]] + str(version[4])

    return main + sub


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='joda-misc',
    version=get_version(joda_misc.VERSION),
    packages=find_packages(),
    include_package_data=True,
    license='AGPL 3.0 License',
    description='Joda Misc Backend',
    long_description=README,
    url='https://tano.si',
    author='Tadej Novak',
    author_email='tadej@tano.si',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
