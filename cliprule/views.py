from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import serializers
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("Hello, world. You're at the cliprule index.")


class ClipRuleList(generics.ListCreateAPIView):
    queryset = models.Clipath.objects.all()
    serializer_class = serializers.ClipRuleSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=201)