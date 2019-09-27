from typing import TYPE_CHECKING, Optional, Tuple

from django.conf import settings

try:
    from ipware import get_client_ip
except ImportError:
    # django-ipware isn't installed
    def get_client_ip(request, *args, **kwargs) -> Tuple[Optional[str], bool]:
        return None, False


if TYPE_CHECKING:
    import google.cloud.error_reporting
    from django.core.handlers.wsgi import WSGIRequest


def build_google_cloud_error_django_context(
    request: "WSGIRequest", response_status_code=500
) -> "google.cloud.error_reporting.HTTPContext":
    """
    Builds a reporting context from a Django request object

    Inspired by google.cloud.error_reporting.util.build_flask_context

    :param request:
    :param response_status_code:
    :return:
    """
    import google.cloud.error_reporting

    client_ip, _ = get_client_ip(request)

    return google.cloud.error_reporting.HTTPContext(
        url=request.get_raw_uri(),
        method=request.method,
        user_agent=request.headers.get("User-Agent"),
        referrer=request.headers.get("Referer"),
        response_status_code=response_status_code,
        remote_ip=client_ip,
    )


def google_cloud_error_report_current_exception(request: "WSGIRequest"):
    """
    Report the current exception as an error to Google Stackdriver Error Reporting,
    intended to be called within the scope of an exception catch -
    particularly from handler500.
    """

    # if CLOUD_ERROR_REPORTING_DISABLED=True, exit before client creation
    if getattr(settings, "CLOUD_ERROR_REPORTING_DISABLED", False):
        return

    import google.cloud.error_reporting

    # The service that this error appears under in GCloud error reporting
    # If not set this will default to "python"
    service_name = getattr(settings, "CLOUD_ERROR_REPORTING_SERVICE_NAME", None)

    client = google.cloud.error_reporting.Client(service=service_name)

    if request.user.is_authenticated:
        user = str(request.user)
    else:
        user = None

    client.report_exception(
        http_context=build_google_cloud_error_django_context(request), user=user
    )
