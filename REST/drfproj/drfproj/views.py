
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class TesView (APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'year_active': 10
        }
        return Response(data)
