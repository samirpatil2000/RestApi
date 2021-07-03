from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import TextSerializer
from api.models import Text
from rest_framework.permissions import IsAuthenticated

# def home(request):
#     return

class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        data=Text.objects.all()
        serializers=TextSerializer(data,many=True)
        return Response(serializers.data)
    def post(self,request,*args,**kwargs):
        serializer=TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

