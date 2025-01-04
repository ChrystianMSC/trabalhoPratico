from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ExampleModel
from .serializers import ExampleModelSerializer

class ExampleView(APIView):
    def get(self, request):
        data = ExampleModel.objects.all()
        serializer = ExampleModelSerializer(data, many=True)
        return Response(serializer.data)