import sys #to handle extra commands from cmd

from django.conf import settings #to configure our app
from django.core.management import execute_from_command_line
#to apply commands

from django.http import HttpResponse #to return something
#U can also import JsonResponse and use it

from django.urls import path #to Route requests

#configuring
settings.configure(
    DEBUG=True,
    SECRET_KEY='itsmeuknow',
    ROOT_URLCONF=__name__,
)

#our view
def index(request):
    return HttpResponse('<h1>Hello World</h1>')

#our urls
urlpatterns = [
    path('', index),
]

#checking if only that specific file is running (not imported in another file)
if __name__ == '__main__':
    execute_from_command_line(sys.argv)
