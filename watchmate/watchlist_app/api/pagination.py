from rest_framework.pagination import PageNumberPagination

class WatchlistPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'p'