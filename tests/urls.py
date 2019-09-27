from django.urls import include, path

import dj_cloud_error

urlpatterns = [path("example/", include("tests.apps.example.urls"))]

handler500 = dj_cloud_error.handler500
