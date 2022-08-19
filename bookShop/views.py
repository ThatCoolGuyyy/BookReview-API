from xml.dom import ValidationErr
from django.shortcuts import get_object_or_404, render
from requests import Response
from rest_framework import generics, viewsets, authentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from bookShop.models import Books, Review
from bookShop.serializers import BookSerializer, ReviewSerializer

class CreateNewBook(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer

class EditBook(generics.RetrieveUpdateDestroyAPIView):
    queryset= Books.objects.all()
    serializer_class = BookSerializer

class CreateNewReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication]
    serializer_class = ReviewSerializer

class EditReview(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
       username = self.kwargs['username']
       return Review.objects.filter(Reviewer=username)
    
