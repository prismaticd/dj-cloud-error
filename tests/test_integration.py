from unittest import mock

from django.test import TestCase
from django.urls import reverse
from tests.apps.example.views import MyException


class TestCloudError(TestCase):
    def test_error(self):
        with mock.patch(
            "google.cloud.error_reporting.Client", autospec=True
        ) as mock_client_class, self.assertRaises(MyException):
            self.client.get(reverse("example:error"))

        mock_client_class.assert_called_once_with(service=None)
        mock_client = mock_client_class()
        mock_client.report_exception.assert_called_once()

    def test_no_error(self):
        with mock.patch(
            "google.cloud.error_reporting.Client", autospec=True
        ) as mock_client_class:
            self.client.get(reverse("example:no_error"))

        mock_client_class.assert_not_called()
