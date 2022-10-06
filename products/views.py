from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from products import serializers

@api_view(['GET'])
def products_list(request):

    return Response('ok')