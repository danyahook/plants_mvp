from enum import Enum

from bitfield import BitField
from django.db import models
from django.utils.text import slugify

SOIL_TYPES = (
    ('clay', 'Clay'),
    ('sand', 'Sand'),
    ('chalk', 'Chalk'),
    ('loam', 'Loam'),
)

SOIL_MOISTURE = (
    ('moist_but_well_drained', 'Moist but well–drained'),
    ('poorly_drained', 'Poorly–drained'),
    ('well_drained', 'Well–drained'),
)

SOIL_PH = (
    ('acid', 'Acid'),
    ('neutral', 'Neutral'),
    ('alkaline', 'Alkaline'),
)

POSITION_SUNLIGHT = (
    ('partial_shade', 'Partial shade'),
    ('full_sun', 'Full sun'),
    ('full_shade', 'Full shade'),
)

POSITION_SIDE = (
    ('east_facing', 'East–facing'),
    ('north_facing', 'North–facing'),
    ('west_facing', 'West–facing'),
    ('south_facing', 'South–facing'),
)


POSITION_EXPOSED = (
    ('exposed', 'Exposed'),
    ('sheltered', 'Sheltered'),
)

SEASONS_LIST = (
    ('winter', 'Winter'),
    ('spring', 'Spring'),
    ('mid_fall', 'Mid fall'),
    ('mid_summer', 'Mid summer'),
    ('summer', 'Summer'),
    ('fall', 'Fall'),
    ('late_fall', 'Late fall'),
    ('all_year_around', 'All year around'),
    ('mid_spring', 'Mid spring'),
    ('mid_winter', 'Mid winter'),
    ('late_summer', 'Late summer'),
    ('early_fall', 'Early fall'),
    ('late_winter', 'Late winter'),
    ('early_summer', 'Early summer'),
    ('late_spring', 'Late spring'),
    ('early_spring', 'Early spring'),
    ('early_winter', 'Early winter'),
)

TOXIC_TYPE = (
    ('toxic_to_cats', 'Toxic to Cats'),
    ('slightly_toxic_to_humans', 'Slightly Toxic to Humans'),
    ('moderate_toxic_to_humans', 'Moderate Toxic to Humans'),
    ('highly_toxic_to_humans', 'Highly Toxic to Humans'),
    ('toxic_to_dogs', 'Toxic to Dogs'),
)


FOLIAGE_TYPE = (
    ('deciduous', 'Deciduous'),
    ('evergreen', 'Evergreen'),
    ('semi_evergreen', 'Semi evergreen'),
)


HABIT_TYPES = (
    ('tufted', 'Tufted'),
    ('trailing', 'Trailing'),
    ('pendulous_weeping', 'Pendulous weeping'),
    ('clump_forming', 'Clump forming'),
    ('columnar_upright', 'Columnar upright'),
    ('submerged', 'Submerged'),
    ('suckering', 'Suckering'),
    ('floating', 'Floating'),
    ('matforming', 'Matforming'),
    ('bushy', 'Bushy'),
    ('climbing', 'Climbing'),
)


class TimeChoices(models.IntegerChoices):
    MINUTE = 1
    HOUR = 2
    DAY = 3
    WEEK = 4
    FORTNIGHT = 5
    MONTH = 6
    YEAR = 7
    CENTURY = 8


class AilmentTypes(Enum):
    disease = 1
    pest = 2


class PlantParts(Enum):
    root = 1
    stem = 2
    foliage = 3
    flower = 4
    fruit = 5
    seed = 6
    tuber = 7


class MinMaxValue(models.Model):
    minimum = models.PositiveIntegerField()
    maximum = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'<MinMax>: from {self.minimum} to {self.maximum}'


class PlantQuerySet(models.QuerySet['Plant']):
    def prefetch_related_all(self) -> 'PlantQuerySet':
        queryset = self
        return queryset.prefetch_related(
            models.Prefetch('regular_events'),
            models.Prefetch('ailments'),
            models.Prefetch('common_names'),
            models.Prefetch('propagations'),
            models.Prefetch('pruning'),
            models.Prefetch('tags'),
            models.Prefetch('synonyms'),
            models.Prefetch('parts_color', queryset=PartColor.objects.prefetch_related('colors_part'))
        )


class Plant(models.Model):
    latin_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    main_common_name_en = models.CharField(max_length=128, unique=True)
    rank = models.PositiveIntegerField(default=0)

    height_cm = models.OneToOneField(MinMaxValue, on_delete=models.CASCADE, related_name='height_cm')
    years_to_max_height = models.OneToOneField(
        MinMaxValue,
        on_delete=models.CASCADE,
        related_name='years_to_max_height'
    )
    spread_cm = models.OneToOneField(MinMaxValue, on_delete=models.CASCADE, related_name='spread_cm')

    soil_type = BitField(
        flags=SOIL_TYPES,
        null=True,
        help_text='BitFlag. The type of soil in which the plant can grow.'
    )
    soil_moisture = BitField(flags=SOIL_MOISTURE, null=True, help_text='BitFlag. Ground humidity level.')
    soil_ph = BitField(flags=SOIL_PH, null=True, help_text='BitFlag. The acidity of the soil required for the plant.')

    position_sunlight = BitField(
        flags=POSITION_SUNLIGHT,
        null=True,
        help_text='BitFlag. The level of sunlight on the plant.'
    )
    position_side = BitField(
        flags=POSITION_SIDE,
        null=True,
        help_text='BitFlag. The side of the world where the plant can grow well.'
    )
    is_sun_exposure = models.BooleanField(
        null=True,
        help_text='Sun-loving or not plant. The amount of light that the plant receives'
    )
    hardiness_zone = models.CharField(max_length=4, blank=True, default='')

    cultivation = models.TextField(blank=True, default='')
    harvest = BitField(flags=SEASONS_LIST, null=True, help_text='BitFlag. The time at which to harvest, if any.')
    planting = BitField(flags=SEASONS_LIST, null=True, help_text='BitFlag. The time at which to plant the plant.')

    toxicity = BitField(
        flags=TOXIC_TYPE,
        null=True,
        help_text='BitFlag. The level of toxicity of the plant to humans and animals.'
    )

    genus_description = models.TextField(blank=True, default='')
    family = models.CharField(max_length=128)
    phylum = models.CharField(max_length=128)
    classify = models.CharField(max_length=128)
    order = models.CharField(max_length=128)
    genus = models.CharField(max_length=128)
    species = models.CharField(max_length=128)

    foliage = BitField(
        flags=FOLIAGE_TYPE,
        null=True,
        help_text='BitFlag. Features regarding seasonal changes in foliage.'
    )
    habit = BitField(
        flags=HABIT_TYPES,
        null=True,
        help_text='BitFlag. '
                  'The general shape and morphology of the plant, its growth method and organization of structures.'
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = PlantQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.latin_name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'<Plant>: {self.slug}'


class RegularEvent(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='regular_events')
    name = models.CharField(max_length=64, unique=True)
    frequency = models.OneToOneField(MinMaxValue, on_delete=models.CASCADE)
    frequency_count = models.PositiveSmallIntegerField(default=1)
    frequency_unit = models.PositiveSmallIntegerField(choices=TimeChoices.choices)

    def __str__(self):
        return f'<PlantEventInfo>: {self.name}'


class BasePlantSpecification(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True)
    description = models.TextField(default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'<{type(self).__name__}>: {self.name}'


class Propagation(BasePlantSpecification):
    plant = models.ManyToManyField(Plant, related_name='propagations')


class Pruning(BasePlantSpecification):
    plant = models.ManyToManyField(Plant, related_name='pruning')


class Ailment(BasePlantSpecification):
    plant = models.ManyToManyField(Plant, related_name='ailments')
    type = models.PositiveSmallIntegerField(choices=[(t.value, t.name) for t in AilmentTypes])  # noqa: A003


class Tag(BasePlantSpecification):
    plant = models.ManyToManyField(Plant, related_name='tags')


class PartColor(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='parts_color')
    plant_part = models.PositiveSmallIntegerField(choices=[(t.value, t.name) for t in PlantParts])

    def __str__(self):
        return f'<PlantColor>: {self.plant_part}'


class Color(models.Model):
    color = models.ManyToManyField(PartColor, related_name='colors_part')
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'<Color>: {self.name}'


class CommonName(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='common_names')
    lang = models.CharField(max_length=2)
    name = models.CharField(max_length=64)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'<CommonName>: {self.lang}::{self.name} (is_main={self.is_main})'


class Synonym(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name='synonyms')
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'<Synonym>: {self.name}'
