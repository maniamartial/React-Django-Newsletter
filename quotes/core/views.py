from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
# Create your views here.


from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.


def ReactViewFunction(ListAPIView):
    objects = React.objects.all()
    return HttpResponse(objects)


class ReactView(ListAPIView):

    serializer_class = ReactSerializer
    queryset = React.objects.all()

    def get(self, request):
        detail = [{"name": detail.name, "details": detail.details}
                  for detail in React.objects.all()]
        return Response(detail)

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
