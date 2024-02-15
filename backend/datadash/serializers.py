from rest_framework.serializers import ModelSerializer

from .models import Channelsummary, Qrev, QrevData, Siteinformation, SlSg


class ChannelsummarySerializer(ModelSerializer):
    class Meta:
        model = Channelsummary
        fields = "__all__"


class QrevSerializer(ModelSerializer):
    class Meta:
        model = Qrev
        fields = "__all__"


class QrevDataSerializer(ModelSerializer):
    class Meta:
        model = QrevData
        fields = "__all__"


class SiteinformatonSerializer(ModelSerializer):
    class Meta:
        model = Siteinformation
        fields = "__all__"


class SlSgSerializer(ModelSerializer):
    class Meta:
        model = SlSg
        fields = "__all__"
