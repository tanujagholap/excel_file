from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Product, ProductSerializer
import pandas as pd


class ProductView(APIView):
    def post(self, request):
        file = request.FILES['file']
        df = pd.read_excel(file)

        serializer = ProductSerializer(data=df.to_dict('records'), many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data imported successfully'})

        else:
            return Response(serializer.errors, status=400)


class Total(APIView):
    pass
