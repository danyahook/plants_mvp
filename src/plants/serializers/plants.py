from rest_framework import serializers

from src.common.serializers import (
    GroupManyRelatedField,
)
from src.plants.models import plants


class MaxMinSerializer(serializers.ModelSerializer):

    class Meta:
        model = plants.MinMaxValue
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


class ScientificClassificationSerializer(serializers.Serializer):
    family = serializers.CharField()
    phylum = serializers.CharField()
    classify = serializers.CharField()
    order = serializers.CharField()
    genus = serializers.CharField()
    species = serializers.CharField()


class BotanicalDetailsSerializer(serializers.Serializer):
    foliage = serializers.ListField(source='foliage.get_selected_labels')
    habit = serializers.ListField(source='habit.get_selected_labels')


class RegularEventSerializer(serializers.ModelSerializer):
    frequency_unit = serializers.CharField(source='get_frequency_unit_display')

    class Meta:
        model = plants.RegularEvent
        fields = ('name', 'frequency', 'frequency_count', 'frequency_unit')


class PlantSerializer(serializers.ModelSerializer):
    common_names = GroupManyRelatedField(group_field='lang', return_field='name', read_only=True)
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
        group_field='get_plant_part_display',
        return_field='colors_part',
        sub_return_field='name',
        read_only=True
    )

    toxicity = serializers.ListField(read_only=True, source='toxicity.get_selected_labels')
    ailments = GroupManyRelatedField(group_field='get_type_display', return_field='name', read_only=True)
    scientific_classification = ScientificClassificationSerializer(read_only=True, source='*')
    botanical_details = BotanicalDetailsSerializer(read_only=True, source='*')

    class Meta:
        model = plants.Plant
        fields = (
            'latin_name',
            'slug',
            'main_common_name_en',
            'rank',
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
            'scientific_classification',
            'botanical_details',
            'created',
            'modified',
        )
