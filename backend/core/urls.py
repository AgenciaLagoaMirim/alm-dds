from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from datadash.views import (ChannelsummaryReadOnlyViewSet,
                            QrevDataReadOnlyViewSet, QrevReadOnlyViewSet,
                            SiteInformationReadOnlyViewSet,
                            SlSgReadOnlyViewSet)

from stamvi.views import SetIndexVeldfViewSet

router = routers.DefaultRouter()
router.register("channel-summary", ChannelsummaryReadOnlyViewSet)
router.register("qrev", QrevReadOnlyViewSet)
router.register("qrev-data", QrevDataReadOnlyViewSet)
router.register("site-information", SiteInformationReadOnlyViewSet)
router.register("sl-sg", SlSgReadOnlyViewSet)

stamvi_router = routers.DefaultRouter()
stamvi_router.register("stamvi", SetIndexVeldfViewSet, basename="stamvi")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/data-dash/", include(router.urls)),
    path("api/v1/stamvi/", include(stamvi_router.urls)),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.authtoken")),
]
