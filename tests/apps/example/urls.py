from django.urls import path

from . import views

urlpatterns = [
    path("ok", views.ok, name="no_error"),
    # View that raises an exception
    path("oh-no", views.oh_no, name="error"),
]

app_name = "example"
