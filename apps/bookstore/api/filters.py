import django_filters

from django_filters.rest_framework import FilterSet

from ..models import Book


class BookFilter(FilterSet):
    author_name = django_filters.AllValuesFilter(field_name='author__username')

    class Meta:
        model = Book
        fields = ('author_name',)