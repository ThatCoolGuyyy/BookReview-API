from rest_framework import serializers

from bookShop.models import Books, Review

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ['id','BookName','Author','publisher','numofPages','bookWebsite', 'reviews']


class ReviewSerializer(serializers.ModelSerializer):
    reviews = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['id','Heading', 'book','description','createDate', 'reviews']