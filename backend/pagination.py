from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('has_previous', self.page.has_previous()),
            ('has_next', self.page.has_next()),
            ('count', self.page.paginator.count),
            ('page', self.page.number),
            ('num_page', self.page.paginator.num_pages),
            ('results', data)
        ]))
