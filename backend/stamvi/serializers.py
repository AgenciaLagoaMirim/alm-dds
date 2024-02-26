from rest_framework.serializers import ModelSerializer


from .models import SetIndexVeldf


class SetIndexVeldfSerializer(ModelSerializer):
  class Meta:
    model = SetIndexVeldf
    fields = "__all__"