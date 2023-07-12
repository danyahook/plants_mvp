from rest_framework import filters, viewsets
from rest_framework.pagination import (
    CursorPagination,
)
from rest_framework.serializers import Serializer

from .models.plants import Plant
from .serializers.plants import (
    PlantDitailSerializer,
    PlantSerializer,
)


class PlantViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['latin_name']
    lookup_field = 'slug'
    pagination_class = CursorPagination

    def get_serializer_class(self):
        return {
            'list': PlantSerializer,
            'retrieve': PlantDitailSerializer,
        }.get(self.action, Serializer)

    def get_queryset(self):
        return {
            'list': Plant.objects.order_by('-rank').all(),
            'retrieve': Plant.objects.related_all().all(),
        }.get(self.action, Plant.objects.none())
