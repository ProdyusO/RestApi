from rest_framework.serializers import ModelSerializer
from .models import AmountOfUpvotes, Author, Comments


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('title', 'link', 'creation_date', 'author')


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class AmountOfUpvotesSerializer(ModelSerializer):
    class Meta:
        model = AmountOfUpvotes
        fields = '__all__'
