from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationClass(PageNumberPagination):

    page_size_query_param = "page_size"

    def get_paginated_response(self, data):

        response = Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "totalPages": self.page.paginator.num_pages,
                "results": data,
            }
        )
        response["X-Pagination"] = "true"
        return response
