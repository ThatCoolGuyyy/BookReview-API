from django.shortcuts import get_object_or_404, render
from requests import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ReviewSerializer


class EditReview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# class createNewView(viewsets.ViewSet):
    
#     def list(self, request):
#         queryset = Review.objects.all()
#         serializer = ReviewSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Review.objects.all()
#         review = get_object_or_404(queryset, pk=pk)
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)

#     def get_extra_actions(cls):
#         return []
