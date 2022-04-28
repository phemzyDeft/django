from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from drfapp.serializers import StudentSerializer
from drfapp.models import Student


class TesView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'year_active': 10
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
