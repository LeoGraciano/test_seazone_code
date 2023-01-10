
from django.urls import include, path
from rest_framework import routers
from apps.immobile import views

router = routers.DefaultRouter()
router.register(r'immobile', views.ImmobileViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
