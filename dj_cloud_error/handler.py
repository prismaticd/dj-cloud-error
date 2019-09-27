import django.conf.urls

from . import utils


def handler500(request):
    """
    Replacement for handler500 that reports errors to GCloud

    Note: this isn't used if DEBUG=True

    To install, import this and assign it as handler500 in the root urls.py

    eg:

    import dj_cloud_error

    handler500 = dj_cloud_error.handler500
    """

    utils.google_cloud_error_report_current_exception(request)

    # run default 500 handler
    return django.conf.urls.handler500(request)
