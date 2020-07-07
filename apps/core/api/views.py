from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response

from apps.bookstore.api.views import BookList


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'books': reverse(BookList.name, request=request),
        })
