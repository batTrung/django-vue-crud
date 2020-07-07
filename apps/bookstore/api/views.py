from django.utils.text import slugify

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status    

from .serializers import BookSerializer
from .filters import BookFilter
from .permissions import IsAuthorReadOnly
from ..models import Book


class BookList(ListCreateAPIView):
    queryset = Book.objects.published()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorReadOnly,
    )
    search_fields = (
        'name',
        'description',
    )
    ordering_fields = (
        'name',
        'created',
        'price',
        'author',
    )
    name = 'book-list'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.published()
    serializer_class = BookSerializer
    lookup_field = 'slug'
    name = 'book-detail'


class BookCheckDuplicateName(APIView):
    name = 'book-check-duplicate-name'

    def get(self, request, book_name, book_slug=None, format=None):
        new_book_slug = slugify(book_name)

        book_exists = Book.objects.published(
            ).exclude(
                slug=book_slug
            ).filter(
                slug=new_book_slug
            ).exists()

        return Response({
            'invalid': book_exists,
        })
