import numpy as np
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from sklearn.linear_model import LinearRegression

from .models import SetIndexVeldf


class DateFieldConverter(serializers.Field):
    def to_representation(self, value):
        # Converte datetime em uma data
        return value.date()


class SetIndexVeldfSerializer(serializers.ModelSerializer):
    data = DateFieldConverter()  # Usa o campo personalizado para lidar com a conversão

    class Meta:
        model = SetIndexVeldf
        fields = "__all__"
