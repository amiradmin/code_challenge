# books/serializers.py

from rest_framework import serializers
from .models import Book,Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class BookSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'user', 'created_at','reserved','status']
        read_only_fields = ['id', 'user', 'created_at']

    def validate_isbn(self, value):
        """
        Check that the book with this ISBN does not already exist.
        """
        if self.instance:  # This means we're updating an instance
            if Book.objects.filter(isbn=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("Book with this ISBN already exists.")
        else:  # We're creating a new instance
            if Book.objects.filter(isbn=value).exists():
                raise serializers.ValidationError("Book with this ISBN already exists.")
        return value


    def create(self, validated_data):
        request = self.context.get('request', None)
        user = None
        if request and hasattr(request, "user"):
            user = request.user
        book = Book.objects.create(user=user, **validated_data)
        return book


    def update(self, instance, validated_data):
        # Handle updating instance fields
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.save()
        return instance


    def delete(self, instance):
        """
        Delete the book instance.We don't have to have it explicitly delete.
        """
        instance.delete()
        return None  # Return None to indicate the deletion was successful

    def get_status(self, obj):
        return obj.get_status()
