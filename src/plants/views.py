from rest_framework import filters, viewsets

from .models.plants import PartColor, Plant
from .serializers.plants import PlantSerializer


class PlantViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Plant.objects \
        .select_related('height_cm', 'years_to_max_height', 'spread_cm') \
        .prefetch_related_all().all()
    serializer_class = PlantSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['latin_name']
    lookup_field = 'slug'
