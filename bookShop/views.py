from django.shortcuts import render
from rest_framework import generics
from bookShop.models import Books, Review
from bookShop.serializers import BookSerializer, ReviewSerializer

class CreateNewBook(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class EditBook(generics.RetrieveUpdateDestroyAPIView):
    queryset= Books.objects.all()
    serializer_class = BookSerializer

class CreateNewReview(generics.ListCreateAPIView):
    lookup_field = 'pk'
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class EditReview(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset= Review.objects.all()
    serializer_class = BookSerializer