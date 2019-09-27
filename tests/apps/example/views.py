from django.http import HttpResponse


class MyException(Exception):
    pass


def ok(request):
    """
    View that doesn't raise
    """
    return HttpResponse("<html><body>OK</body></html>")


def oh_no(request):
    """
    View that raises an exception
    """
    raise MyException("oh no")
