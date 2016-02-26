from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_mongoengine import viewsets as mongo_viewsets

from api import models, serializers, utils


class ParselStatus(APIView):

    def get(self, request, parsel_code):
        parsel_status = utils.get_parsel_status(parsel_code)
        package = models.Package(**parsel_status)
        serializer = serializers.PackageSerializer(package)
        return Response(serializer.data)


class ParselViewSet(mongo_viewsets.ModelViewSet):
    pass
