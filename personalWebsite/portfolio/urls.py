from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
# From the path function
# '' means a root
# views.index means invokes the function called index from views
# name='index' means an id of specific path