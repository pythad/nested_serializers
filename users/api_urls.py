from django.urls import path

from . import api


urlpatterns = [
    path('', api.MyUserList.as_view()),
]
