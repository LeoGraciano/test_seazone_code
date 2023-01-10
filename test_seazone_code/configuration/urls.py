from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('immobile/', include('apps.immobile.urls')),
    path('announcement/', include('apps.announcement.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
