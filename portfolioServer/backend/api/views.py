from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExampleModel, Color
from .serializers import ExampleModelSerializer, ColorSerializer

class ExampleView(APIView):
    def get(self, request):
        data = ExampleModel.objects.all()
        serializer = ExampleModelSerializer(data, many=True)
        return Response(serializer.data)

class ColorListCreateView(APIView):
    def get(self, request):
        colors = Color.objects.all()
        serializer = ColorSerializer(colors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)