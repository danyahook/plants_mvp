from bitfield import BitField
from bitfield.forms import (
    BitFieldCheckboxSelectMultiple,
)
from django.contrib import admin

from .models.plants import (
    Ailment,
    Color,
    CommonName,
    MinMaxValue,
    PartColor,
    Plant,
    Propagation,
    Pruning,
    RegularEvent,
    Synonym,
    Tag,
)

admin.site.register(MinMaxValue)
admin.site.register(RegularEvent)
admin.site.register(Propagation)
admin.site.register(Pruning)
admin.site.register(Ailment)
admin.site.register(Tag)
admin.site.register(Color)
admin.site.register(PartColor)
admin.site.register(CommonName)
admin.site.register(Synonym)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    formfield_overrides = {
            BitField: {'widget': BitFieldCheckboxSelectMultiple},
    }

    readonly_fields = ('slug',)
