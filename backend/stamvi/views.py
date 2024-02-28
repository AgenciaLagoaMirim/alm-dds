import numpy as np
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from sklearn.linear_model import LinearRegression

from .models import SetIndexVeldf
from .serializers import SetIndexVeldfSerializer


class SetIndexVeldfViewSet(ReadOnlyModelViewSet):
  serializer_class = SetIndexVeldfSerializer
  queryset = SetIndexVeldf.objects.all()


class SetIndexVeldfRegressionViewSet(viewsets.ViewSet):
  def list(self, request):
        # Obtenha os dados de SetIndexVeldf
        queryset = SetIndexVeldf.objects.all()

        # Extrair os valores de level e mean_area
        levels = [entry.level for entry in queryset]
        mean_areas = [entry.mean_area for entry in queryset]

        # Converta os dados para numpy arrays e redimensione-os para o formato correto
        X = np.array(levels).reshape(-1, 1)  # Shape: (n_samples, n_features)
        y = np.array(mean_areas)  # Shape: (n_samples,)

        # Instancie e ajuste o modelo de regressão linear
        model = LinearRegression()
        model.fit(X, y)

        # Coletar os coeficientes do modelo
        coeficiente_angular = model.coef_[0]
        intercepto = model.intercept_

        # Retorne os resultados da regressão linear
        return Response(
            {"coeficiente_angular": coeficiente_angular, "intercepto": intercepto},
            status=status.HTTP_200_OK,
        )
