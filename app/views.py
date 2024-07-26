import os
from django.http import HttpResponse


def index(request):
    app_name = os.environ.get('APP_NAME')
    return HttpResponse("Welcome to the " + app_name.title() + " App!")
