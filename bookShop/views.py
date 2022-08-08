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
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class EditReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # def get_queryset(self):  
    #     review = Review.objects.get(pk=self.kwargs.get('pk', None))
    #     movies = Review.objects.filter(review=review)
    #     return movies