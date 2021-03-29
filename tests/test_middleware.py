from unittest import mock

from django.test import TestCase, modify_settings, override_settings
from django.urls import reverse

from tests.apps.example.views import MyException


class TestMiddleware(TestCase):
    def setUp(self):
        self.exception = Exception()

    @modify_settings(
        MIDDLEWARE={
            "append": "dj_cloud_error.middleware.GoogleCloudMiddleware",
        }
    )
    @override_settings(DEBUG=False)
    def test_process_exception(self):
        with mock.patch(
            "google.cloud.error_reporting.Client", autospec=True
        ) as mock_client_class, self.assertRaises(MyException):
            self.client.get(reverse("example:error"))

        mock_client_class.assert_called()
        mock_client = mock_client_class()
        mock_client.report_exception.assert_called()
