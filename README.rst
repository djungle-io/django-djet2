============
Django DJET2
============

Django admin interface based on django-jet (and django-jet2) forked for recent Django.

.. image:: https://raw.githubusercontent.com/djungle-io/django-djet2/master/docs/_static/logo.png
    :width: 500px
    :height: 500px
    :scale: 50%
    :alt: Logo
    :align: center

* Home page: https://github.com/djungle-io/django-djet2
* PyPI: https://pypi.python.org/pypi/django-djet2

Why Django JET?
===============

* New fresh look
* Responsive mobile interface
* Useful admin home page
* Minimal template overriding
* Easy integration
* Themes support
* Autocompletion
* Handy controls

Screenshots
===========

Index dashboard

.. image:: https://raw.githubusercontent.com/djungle-io/django-djet2/master/docs/_static/screen1_720.png
    :alt: Screenshot #1
    :align: center
    :target: https://raw.githubusercontent.com/djungle-io/django-djet2/master/docs/_static/screen1.png

Changelist

.. image:: https://raw.githubusercontent.com/djungle-io/django-djet2/master/docs/_static/screen2_720.png
    :alt: Screenshot #2
    :align: center
    :target: https://raw.githubusercontent.com/djungle-io/django-djet2/master/docs/_static/screen2.png

Sidemenu

.. image:: https://raw.githubusercontent.com/djungle-io/django-djet2/master/docs/_static/screen3_720.png
    :alt: Screenshot #3
    :align: center
    :target: https://raw.githubusercontent.com/djungle-io/django-djet2/master/docs/_static/screen3.png

Installation
============

* Download and install latest version of Django JET:

.. code:: python

    pip install django-djet2

* Add 'jet' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'django.contrib.admin'):

.. code:: python

    INSTALLED_APPS = (
        ...
        'jet',
        'django.contrib.admin',
    )

* Make sure ``django.template.context_processors.request`` context processor is enabled in settings.py (Django 1.8+ way):

.. code:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    'django.template.context_processors.request',
                    ...
                ],
            },
        },
    ]

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):

.. code:: python

    urlpatterns = patterns(
        '',
        path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
        path('admin/', include(admin.site.urls)),
        ...
    )

* Create database tables:

.. code:: python

    python manage.py migrate jet

* Collect static if you are in production environment:

.. code:: python

        python manage.py collectstatic

* Clear your browser cache

Dashboard installation
======================

.. note:: Dashboard is located into a separate application. So after a typical JET installation it won't be active.
          To enable dashboard application follow these steps:

* Add 'jet.dashboard' application to the INSTALLED_APPS setting of your Django project settings.py file (note it should be before 'jet'):

.. code:: python

    INSTALLED_APPS = (
        ...
        'jet.dashboard',
        'jet',
        'django.contrib.admin',
        ...
    )

* Add URL-pattern to the urlpatterns of your Django project urls.py file (they are needed for related–lookups and autocompletes):

.. code:: python

    urlpatterns = patterns(
        '',
        path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
        path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
        path('admin/', include(admin.site.urls)),
        ...
    )

* **For Google Analytics widgets only** install python package:

.. code::

    pip install google-api-python-client==1.4.1

* Create database tables:

.. code:: python

    python manage.py migrate dashboard

* Collect static if you are in production environment:

.. code:: python

        python manage.py collectstatic

License
=======

Django JET (which Django JET2 is based on) has two kinds of licenses: open-source (AGPLv3) and commercial. Please note that using AGPLv3
code in your programs make them AGPL compatible too. So if you don't want to comply with that we can provide you
a commercial license (visit Home page). The commercial license is designed for using Django JET in commercial products
and applications without the provisions of the AGPLv3.
