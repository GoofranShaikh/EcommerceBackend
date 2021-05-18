from os import name
from django.db.models.fields import SlugField
from django.shortcuts import Http404
from rest_framework import response

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import products,category
from .serializers import productsSerializer,categorySerializer
from django.http import HttpResponse

#for showing category dropdown
@api_view(['GET'])
def getCategory(request):
    categories=category.objects.all()
    serializer=categorySerializer(categories, many=True)
    return Response(serializer.data)

#get all the products under the specific category 
@api_view(['GET'])
def getSelectedCategory(request,categories,query):
    
    selectedCategory=products.objects.filter(category=query)
    serializer=productsSerializer(selectedCategory,many=True)
    return Response(serializer.data)

#page for all the products
class LatestProductsList(APIView):
    def get(self, request, format=None):
        Product=products.objects.all()[0:4]
        serializer=productsSerializer(Product,many=True)
        return Response(serializer.data)



# product description page
class viewProduct(APIView):
    def get_products(self, categoryslug, productslug):
        try:
            return products.objects.filter(category__slug=categoryslug).get(slug=productslug)
        except products.DoesNotExist:
            return Http404 

    def get( self , request, categoryslug, productslug, format=None):
        product=self.get_products(categoryslug,productslug) 
        serializer=productsSerializer(product)
        return Response(serializer.data)


#getting the product enter in searchbox by the user
@api_view(['GET'])
def userSearch(request,query):
       
    search=products.objects.filter(name__icontains= query)
    serializer=productsSerializer(search,many=True)
    return Response(serializer.data)



