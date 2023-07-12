from datetime import datetime

from rest_framework import serializers

from src.common.serializers.fields import (
    GroupManyRelatedField,
)
from src.plants.models.plants import (
    MinMaxValue,
    Plant,
    RegularEvent,
)


class MaxMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = MinMaxValue
        fields = ('maximum', 'minimum')


class SizeSerializer(serializers.Serializer):
    height_cm = MaxMinSerializer()
    years_to_max_height = MaxMinSerializer()
    spread_cm = MaxMinSerializer()


class SoilSerializer(serializers.Serializer):
    type = serializers.ListField(source='soil_type.get_selected_labels')    # noqa: A003
    moisture = serializers.ListField(source='soil_moisture.get_selected_labels')
    ph = serializers.ListField(source='soil_ph.get_selected_labels')


class PositionSerializer(serializers.Serializer):
    sunlight = serializers.ListField(source='position_sunlight.get_selected_labels')
    side = serializers.ListField(source='position_side.get_selected_labels')
    is_sun_exposure = serializers.BooleanField()
    hardiness_zone = serializers.ReadOnlyField()


class EventsSerializer(serializers.Serializer):
    harvest = serializers.ListField(source='harvest.get_selected_labels')
    planting = serializers.ListField(source='planting.get_selected_labels')


class BotanicalDetailsSerializer(serializers.Serializer):
    foliage = serializers.ListField(source='foliage.get_selected_labels')
    habit = serializers.ListField(source='habit.get_selected_labels')


class RegularEventSerializer(serializers.ModelSerializer):
    frequency_unit = serializers.CharField(source='get_frequency_unit_display')

    class Meta:
        model = RegularEvent
        fields = ('name', 'frequency', 'frequency_count', 'frequency_unit')


class PlantSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plant-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Plant
        fields: tuple[str, ...] = (
            'latin_name',
            'slug',
            'url',
            'main_common_name_en',
            'rank',
            'family',
            'phylum',
            'classify',
            'order',
            'genus',
            'species',
            'created',
            'modified',
        )


class PlantDitailSerializer(PlantSerializer):
    common_names = GroupManyRelatedField(read_only=True, group_field='lang', return_field='name')
    synonyms = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    size = SizeSerializer(read_only=True, source='*')
    soil = SoilSerializer(read_only=True, source='*')
    position = PositionSerializer(read_only=True, source='*')

    events = EventsSerializer(read_only=True, source='*')
    regular_events = RegularEventSerializer(many=True, read_only=True)

    propagations = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    pruning = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    parts_color = GroupManyRelatedField(
        read_only=True,
        group_field='get_plant_part_display',
        return_field='colors_part',
        sub_return_field='name',
    )

    toxicity = serializers.ListField(read_only=True, source='toxicity.get_selected_labels')
    ailments = GroupManyRelatedField(read_only=True, group_field='get_type_display', return_field='name')
    botanical_details = BotanicalDetailsSerializer(read_only=True, source='*')

    class Meta(PlantSerializer.Meta):
        fields: tuple[str, ...] = (
            *PlantSerializer.Meta.fields,
            'common_names',
            'synonyms',
            'tags',
            'genus_description',
            'size',
            'soil',
            'position',
            'events',
            'regular_events',
            'cultivation',
            'propagations',
            'pruning',
            'toxicity',
            'parts_color',
            'ailments',
            'botanical_details',
        )
