from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "pk",
            "title",
            "num_pages",
            "pub_date",
            "price",
            "color",
            "isbn13",
        ]

        extra_kwargs = {
            "pub_date": {"required": False},
            "price": {"required": False},
            "color": {"required": False},
            "isbn13": {"required": False},
        }
