from rest_framework import serializers

from ..models import Book


class UserPhotoForeignKey(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return get_user_model().objects.all()


class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='slug')
    author = serializers.ReadOnlyField(source='author.username')
    timesince = serializers.CharField(source="timeago", read_only=True)
    status_description = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Book
        fields = (
            'url',
            'author',
            'name',
            'timesince',
            'slug',
            'status',
            'description',
            'status_description',
            'views',
            'created',
            'price',
            'photo',
        )

