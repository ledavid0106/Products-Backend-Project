from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework. response import Response
from rest_framework import status

from products.models import Product
from .serializer import ReviewSerializer
from .models import Review
from product_reviews import serializer

@api_view(['GET', 'POST'])
def reviews_list(request):

    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)    
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def view_review(request,pk):

    product = Product.objects.get(pk)
    view = Review.objects.get(product_id=product.pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(view)
        return Response(serializer.data)
    # view_review = get_object_or_404(Review, fk=pk)
    # if request.method == 'GET':
    #     serializer = ReviewSerializer(view_review)
    #     return Response(serializer.data)