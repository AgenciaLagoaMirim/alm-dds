from django.urls import include, path
from rest_framework import routers

from datadash.views import (
    ChannelsummaryReadOnlyViewSet,
    QrevDataReadOnlyViewSet,
    QrevReadOnlyViewSet,
    SiteInformationReadOnlyViewSet,
    SlSgReadOnlyViewSet,
)

data_dash_router = routers.DefaultRouter()
data_dash_router.register("channel-summary", ChannelsummaryReadOnlyViewSet)
data_dash_router.register("qrev", QrevReadOnlyViewSet)
data_dash_router.register("qrev-data", QrevDataReadOnlyViewSet)
data_dash_router.register("site-information", SiteInformationReadOnlyViewSet)
data_dash_router.register("sl-sg", SlSgReadOnlyViewSet)
