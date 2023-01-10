
from django.urls import include, path
from rest_framework import routers
from apps.reserve import views

router = routers.DefaultRouter()
router.register(r'api/v1', views.ReserveViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
