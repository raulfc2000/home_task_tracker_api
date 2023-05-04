import math

from django.core.paginator import Paginator
from django.utils.functional import cached_property
from rest_framework import pagination
from rest_framework.response import Response
from math import ceil


class CustomPagination(pagination.PageNumberPagination):
    """
    Class to set pagination in the response
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500

    def get_count(self, queryset):
        """
        Determine an object count, supporting either querysets or regular lists.
        """
        try:
            return queryset.values('id').count()
        except (AttributeError, TypeError):
            return len(queryset)

    def get_paginated_response(self, data):
        per_page = len(data)
        if per_page > 0:
            last_page = math.ceil(self.page.paginator.count/per_page)
            return Response({
                'lastPage': last_page,
                'currentPage': self.page.number,
                'perPage': self.get_page_size(self.request),
                'total': self.page.paginator.count,
                'data': data
            })
        else:
            return Response({
                'lastPage': 0,
                'currentPage': 0,
                'perPage': 0,
                'total': 0,
                'data': data
            })


class NoCountPaginator(Paginator):

    # TODO estas tres funciones son las que estan usando el count y las que realientizan

    @cached_property
    def count(self):
        # only select 'id' for counting, much cheaper
        return self.object_list.values('id').count()

    def page(self, number):
        """Return a Page object for the given 1-based page number."""
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        return self._get_page(self.object_list[bottom:top], number, self)

    @cached_property
    def num_pages(self):
        """Return the total number of pages."""
        if self.count == 0 and not self.allow_empty_first_page:
            return 0
        hits = max(1, self.count - self.orphans)
        return ceil(hits / self.per_page)


class CustomWithoutCountPagination(pagination.PageNumberPagination):
    """
    Class to set pagination in the response
    """

    django_paginator_class = NoCountPaginator  # TODO volver a poner cuando el Paginator custom no haga count y funcione bien
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 500

    def get_paginated_response(self, data):
        per_page = len(data)
        if per_page > 0:
            #last_page = math.ceil(self.page.paginator.count/per_page)
            return Response({
                'currentPage': self.page.number,
                'perPage': self.page_size,
                'data': data
            })
        else:
            return Response({
                'currentPage': 0,
                'perPage': 0,
                'data': data
            })
