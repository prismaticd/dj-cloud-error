import os

from google.cloud import error_reporting


class GoogleCloudMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        service = os.environ.get("GOOGLE_CLOUD_ERROR_SERVICE", None)
        version = os.environ.get("GOOGLE_CLOUD_ERROR_VERSION", None)
        self.client = error_reporting.Client(service=service, version=version)

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        self.client.report_exception()
        return None
