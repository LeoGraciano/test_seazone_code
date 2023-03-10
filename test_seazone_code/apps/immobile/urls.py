
from django.urls import include, path
from rest_framework import routers
from apps.immobile import views

router = routers.DefaultRouter()
router.register(r'api/v1', views.ImmobileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
