
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class GeneralApiView(APIView):
    def get(self, request, format=None):
       return Response("serializer.data", status.HTTP_200_OK)
    
    