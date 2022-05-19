import os
from setuptools import setup, find_packages


def read(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    try:
        file = open(path, encoding='utf-8')
    except TypeError:
        file = open(path)
    return file.read()


setup(
    name='django-djet2',
    version=__import__('jet').__version__,
    description='Next Generation of django-jet (Modern template for Django admin interface with improved functionality)',
    long_description=read('README.rst'),
    url='https://github.com/djungle-io/django-djet2',
    maintainer='Djungle Studio',
    maintainer_email='tech@djungle.io',
    packages=find_packages(),
    license='AGPLv3',
    python_requires='>=3',
    keywords=['django', 'admin'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Environment :: Web Environment',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
    zip_safe=False,
    include_package_data=True,
    install_requires=['Django'],
    long_description_content_type='text/x-rst',
    project_urls={
        'Source': 'https://github.com/djungle-io/django-djet2',
        'Tracker': 'https://github.com/djungle-io/django-djet2/issues',
    },
)
