===================================================
dj-cloud-error: Django Google Cloud Error Reporting
===================================================


.. image:: https://img.shields.io/pypi/v/dj_cloud_error.svg
        :target: https://pypi.python.org/pypi/dj_cloud_error

.. image:: https://img.shields.io/travis/prismaticd/dj-cloud-error.svg
        :target: https://travis-ci.org/prismaticd/dj-cloud-error





Report exceptions from any Django site to Google Cloud Stackdriver Error Reporting


* Free software: MIT license


Features
--------

* Report exceptions from any Django site to Google Cloud Stackdriver Error Reporting
* Optional dependency on django-ipware for logging of IP addresses

Quickstart
----------

1) Configure your app to user Google Cloud project:

 * Enabled the Error Reporting api as per https://cloud.google.com/error-reporting/docs/setup/python
 * Set up the required Google IAM credentials - eg set the environment variable GOOGLE_APPLICATION_CREDENTIALS
   as the path to a service account JSON file, for an account that has the "Errors Writer" permission.

2) Install the package::

    pip install dj_cloud_error


3) Enable the provided exception handler by setting ``handler500`` in your Django project's root ``urls.py``::

    # in myproject/urls.py
    import dj_cloud_error

    handler500 = dj_cloud_error.handler500

Note: ``handler500`` is only used if ``DEBUG = False`` in django settings.

Settings
========

To disable error reporting (eg in your CI/CD environment), add this to your django settings::

    # in myproject/settings/test.py
    CLOUD_ERROR_REPORTING_DISABLED = True

To configure the name under which the errors appear in add this to your django settings::


    CLOUD_ERROR_REPORTING_SERVICE_NAME = "myservice"  # defaults to "python"


Optional Extras
===============

If `django-ipware` is installed it's used to log the client IP address, it can be installed as follows::

    pip install dj_cloud_error[ip]

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
