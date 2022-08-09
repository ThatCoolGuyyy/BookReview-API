from rest_framework import serializers
from bookShop.models import Books, Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    Reviewer = serializers.SlugRelatedField(read_only=True,slug_field='username')
    book = serializers.SlugRelatedField(read_only=True,slug_field='BookName')
    class Meta:
        model = Review
        fields = ['Heading','description','createDate', 'Reviewer', 'book']

class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Books
        fields = ['id','Author', 'BookName','publisher','numofPages', 'bookWebsite','reviews']


