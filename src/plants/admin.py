from bitfield import BitField
from bitfield.forms import (
    BitFieldCheckboxSelectMultiple,
)
from django.contrib import admin

from .models import plants

admin.site.register(plants.MinMaxValue)
admin.site.register(plants.RegularEvent)
admin.site.register(plants.Propagation)
admin.site.register(plants.Pruning)
admin.site.register(plants.Ailment)
admin.site.register(plants.Tag)
admin.site.register(plants.Color)
admin.site.register(plants.PartColor)
admin.site.register(plants.CommonName)
admin.site.register(plants.Synonym)


@admin.register(plants.Plant)
class PlantAdmin(admin.ModelAdmin):
    formfield_overrides = {
            BitField: {'widget': BitFieldCheckboxSelectMultiple},
    }

    readonly_fields = ('slug',)
