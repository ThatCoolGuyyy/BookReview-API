from rest_framework import serializers
from bookShop.models import Books, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['Heading','description','createDate']

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Books
        fields = ['BookName','Author','publisher','numofPages','bookWebsite', 'reviews']


