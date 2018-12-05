from rest_framework import filters


class IsUserFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(id=request.user.id) if request.user.is_authenticated else queryset.none()
