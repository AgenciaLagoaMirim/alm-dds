from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from datadash.views import (
    ChannelsummaryReadOnlyViewSet,
    QrevReadOnlyViewSet,
    QrevDataReadOnlyViewSet,
    SiteInformationReadOnlyViewSet,
    SlSgReadOnlyViewSet,
)

router = routers.DefaultRouter()
router.register('channel-summary', ChannelsummaryReadOnlyViewSet)
router.register('qrev', QrevReadOnlyViewSet)
router.register('qrev-data', QrevDataReadOnlyViewSet)
router.register('site-information', SiteInformationReadOnlyViewSet)
router.register('sl-sg', SlSgReadOnlyViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/data-dash/", include(router.urls)),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.authtoken")),
]