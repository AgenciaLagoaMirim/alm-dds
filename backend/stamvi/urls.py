from django.urls import include, path
from rest_framework import routers

from .views import SetIndexVeldfRegressionViewSet, SetIndexVeldfViewSet

stamvi_router = routers.DefaultRouter()
stamvi_router.register("setindexvel", SetIndexVeldfViewSet)
stamvi_router.register("regression", SetIndexVeldfRegressionViewSet, basename="setindexveldf-regression")
