
from django.urls import include, path
from rest_framework import routers
from apps.announcement import views

router = routers.DefaultRouter()
router.register(r'api/v1', views.AnnouncementViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
