from rest_framework.pagination import PageNumberPagination

class InfiniteScrollPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        pass
