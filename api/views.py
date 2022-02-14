from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Product
from .serializers import ProductSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def all_products(request):

    if request.method == "GET":
        products = Product.objects.all()
        products_ser = ProductSerializer(products,many=True)
        return JsonResponse(products_ser.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=200)


@csrf_exempt
def product_detail(self, request, pk):
    try:
        product = Product.objects.get(pk=pk)
    
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        product_ser = ProductSerializer(product)
        return JsonResponse(product_ser.data)
    
    elif request.method == "PUT":
        item = JSONParser().parse(request)
        serializer = ProductSerializer(Product, data=item)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)