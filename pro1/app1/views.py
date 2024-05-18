from django.db.models import Sum
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Product, ProductSerializer
import pandas as pd
from rest_framework.parsers import MultiPartParser


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


class TotalCalculationAPIView(APIView):
    def get(self, request):
        obj = Product.objects.aggregate(total_sum=Sum('price'))
        return Response(data=obj, status=200)


class ProductUpdate(APIView):
    def put(self, request, pk):
        obj = Product.objects.get(id=pk)
        serializers = ProductSerializer(data=request.data, instance=obj, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=200)
        return Response(serializers.errors, status=400)


class ProductDelete(APIView):
    def delete(self, request, pk):
        obj = Product.objects.get(id=pk)
        obj.delete()
        return Response(data={'msg': 'deleted successfully'}, status=200)

