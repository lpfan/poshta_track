from rest_framework.response import Response
from rest_framework.views import APIView

from api import utils


class ParselStatus(APIView):

    def get(self, request, parsel_code):
        parsel_status = utils.get_parsel_status(parsel_code)
        return Response({'status': parsel_status})
