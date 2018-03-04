from django.urls import include, path


urlpatterns = [
    path('users/', include('users.api_urls')),
]
