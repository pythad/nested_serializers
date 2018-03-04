from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('nested_serializers.api_urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
