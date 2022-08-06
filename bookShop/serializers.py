from rest_framework import serializers

from bookShop.models import Books, Review

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    reviews = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = "__all__"