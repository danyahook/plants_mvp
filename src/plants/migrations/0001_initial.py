# Generated by Django 4.2.2 on 2023-07-11 21:23

import bitfield.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MinMaxValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum', models.PositiveIntegerField()),
                ('maximum', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latin_name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('main_common_name_en', models.CharField(max_length=128, unique=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('soil_type', bitfield.models.BitField((('clay', 'Clay'), ('sand', 'Sand'), ('chalk', 'Chalk'), ('loam', 'Loam')), default=None, help_text='BitFlag. The type of soil in which the plant can grow.', null=True)),
                ('soil_moisture', bitfield.models.BitField((('moist_but_well_drained', 'Moist but well–drained'), ('poorly_drained', 'Poorly–drained'), ('well_drained', 'Well–drained')), default=None, help_text='BitFlag. Ground humidity level.', null=True)),
                ('soil_ph', bitfield.models.BitField((('acid', 'Acid'), ('neutral', 'Neutral'), ('alkaline', 'Alkaline')), default=None, help_text='BitFlag. The acidity of the soil required for the plant.', null=True)),
                ('position_sunlight', bitfield.models.BitField((('partial_shade', 'Partial shade'), ('full_sun', 'Full sun'), ('full_shade', 'Full shade')), default=None, help_text='BitFlag. The level of sunlight on the plant.', null=True)),
                ('position_side', bitfield.models.BitField((('east_facing', 'East–facing'), ('north_facing', 'North–facing'), ('west_facing', 'West–facing'), ('south_facing', 'South–facing')), default=None, help_text='BitFlag. The side of the world where the plant can grow well.', null=True)),
                ('is_sun_exposure', models.BooleanField(help_text='Sun-loving or not plant. The amount of light that the plant receives', null=True)),
                ('hardiness_zone', models.CharField(blank=True, default='', max_length=4)),
                ('cultivation', models.TextField(blank=True, default='')),
                ('harvest', bitfield.models.BitField((('winter', 'Winter'), ('spring', 'Spring'), ('mid_fall', 'Mid fall'), ('mid_summer', 'Mid summer'), ('summer', 'Summer'), ('fall', 'Fall'), ('late_fall', 'Late fall'), ('all_year_around', 'All year around'), ('mid_spring', 'Mid spring'), ('mid_winter', 'Mid winter'), ('late_summer', 'Late summer'), ('early_fall', 'Early fall'), ('late_winter', 'Late winter'), ('early_summer', 'Early summer'), ('late_spring', 'Late spring'), ('early_spring', 'Early spring'), ('early_winter', 'Early winter')), default=None, help_text='BitFlag. The time at which to harvest, if any.', null=True)),
                ('planting', bitfield.models.BitField((('winter', 'Winter'), ('spring', 'Spring'), ('mid_fall', 'Mid fall'), ('mid_summer', 'Mid summer'), ('summer', 'Summer'), ('fall', 'Fall'), ('late_fall', 'Late fall'), ('all_year_around', 'All year around'), ('mid_spring', 'Mid spring'), ('mid_winter', 'Mid winter'), ('late_summer', 'Late summer'), ('early_fall', 'Early fall'), ('late_winter', 'Late winter'), ('early_summer', 'Early summer'), ('late_spring', 'Late spring'), ('early_spring', 'Early spring'), ('early_winter', 'Early winter')), default=None, help_text='BitFlag. The time at which to plant the plant.', null=True)),
                ('toxicity', bitfield.models.BitField((('toxic_to_cats', 'Toxic to Cats'), ('slightly_toxic_to_humans', 'Slightly Toxic to Humans'), ('moderate_toxic_to_humans', 'Moderate Toxic to Humans'), ('highly_toxic_to_humans', 'Highly Toxic to Humans'), ('toxic_to_dogs', 'Toxic to Dogs')), default=None, help_text='BitFlag. The level of toxicity of the plant to humans and animals.', null=True)),
                ('genus_description', models.TextField(blank=True, default='')),
                ('family', models.CharField(max_length=128)),
                ('phylum', models.CharField(max_length=128)),
                ('classify', models.CharField(max_length=128)),
                ('order', models.CharField(max_length=128)),
                ('genus', models.CharField(max_length=128)),
                ('species', models.CharField(max_length=128)),
                ('foliage', bitfield.models.BitField((('deciduous', 'Deciduous'), ('evergreen', 'Evergreen'), ('semi_evergreen', 'Semi evergreen')), default=None, help_text='BitFlag. Features regarding seasonal changes in foliage.', null=True)),
                ('habit', bitfield.models.BitField((('tufted', 'Tufted'), ('trailing', 'Trailing'), ('pendulous_weeping', 'Pendulous weeping'), ('clump_forming', 'Clump forming'), ('columnar_upright', 'Columnar upright'), ('submerged', 'Submerged'), ('suckering', 'Suckering'), ('floating', 'Floating'), ('matforming', 'Matforming'), ('bushy', 'Bushy'), ('climbing', 'Climbing')), default=None, help_text='BitFlag. The general shape and morphology of the plant, its growth method and organization of structures.', null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('height_cm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='height_cm', to='plants.minmaxvalue')),
                ('spread_cm', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='spread_cm', to='plants.minmaxvalue')),
                ('years_to_max_height', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='years_to_max_height', to='plants.minmaxvalue')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('plant', models.ManyToManyField(related_name='tags', to='plants.plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='synonyms', to='plants.plant')),
            ],
        ),
        migrations.CreateModel(
            name='RegularEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('frequency_count', models.PositiveSmallIntegerField(default=1)),
                ('frequency_unit', models.PositiveSmallIntegerField(choices=[(1, 'Minute'), (2, 'Hour'), (3, 'Day'), (4, 'Week'), (5, 'Fortnight'), (6, 'Month'), (7, 'Year'), (8, 'Century')])),
                ('frequency', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='plants.minmaxvalue')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regular_events', to='plants.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Pruning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('plant', models.ManyToManyField(related_name='pruning', to='plants.plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Propagation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('plant', models.ManyToManyField(related_name='propagations', to='plants.plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_part', models.PositiveSmallIntegerField(choices=[(1, 'root'), (2, 'stem'), (3, 'foliage'), (4, 'flower'), (5, 'fruit'), (6, 'seed'), (7, 'tuber')])),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts_color', to='plants.plant')),
            ],
        ),
        migrations.CreateModel(
            name='CommonName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=64)),
                ('is_main', models.BooleanField(default=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='common_names', to='plants.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('color', models.ManyToManyField(related_name='colors_part', to='plants.partcolor')),
            ],
        ),
        migrations.CreateModel(
            name='Ailment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'disease'), (2, 'pest')])),
                ('plant', models.ManyToManyField(related_name='ailments', to='plants.plant')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]