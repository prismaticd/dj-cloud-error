from unittest import mock

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from google.cloud.error_reporting.client import HTTPContext

import dj_cloud_error.utils


class TestBuildContext(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_simple_build(self):
        request = self.request_factory.get("/foo")

        context = dj_cloud_error.utils.build_google_cloud_error_django_context(request)

        self.assertIsInstance(context, HTTPContext)
        self.assertEqual(context.url, "http://testserver/foo")
        self.assertEqual(context.method, "GET")
        self.assertEqual(context.responseStatusCode, 500)


class TestReport(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()

    def test_simple_report(self):
        request = self.request_factory.get("/foo")
        request.user = AnonymousUser()

        with mock.patch(
            "google.cloud.error_reporting.Client", autospec=True
        ) as mock_client_class:
            dj_cloud_error.utils.google_cloud_error_report_current_exception(request)

        mock_client_class.assert_called_once_with(service=None)
        mock_client = mock_client_class()
        mock_client.report_exception.assert_called_once()
