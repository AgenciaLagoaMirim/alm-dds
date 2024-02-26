from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Channelsummary, Qrev, QrevData, Siteinformation, SlSg
from .serializers import (ChannelsummarySerializer, QrevDataSerializer,
                          QrevSerializer, SiteinformatonSerializer,
                          SlSgSerializer)


class ChannelsummaryReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = ChannelsummarySerializer
    queryset = Channelsummary.objects.all()


class QrevReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = QrevSerializer
    queryset = Qrev.objects.all()


class QrevDataReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = QrevDataSerializer
    queryset = QrevData.objects.all()


class SiteInformationReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = SiteinformatonSerializer
    queryset = Siteinformation.objects.all()


class SlSgReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = SlSgSerializer
    queryset = SlSg.objects.all()
