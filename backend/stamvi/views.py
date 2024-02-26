from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action


from .serializers import SetIndexVeldfSerializer
from .models import SetIndexVeldf

class SetIndexVeldfViewSet(ViewSet):
  serializer_class = SetIndexVeldfSerializer
  queryset = SetIndexVeldf.objects.all()

  @action(detail=False, methods=['get'])
  def regression_velx_height(self, request):
    dataset = self.queryset
    serializer = self.serializer_class(dataset, many=True)
    print(serializer.data)

    return Response(serializer.data)
