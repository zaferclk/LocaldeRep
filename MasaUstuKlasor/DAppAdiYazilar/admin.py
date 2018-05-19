from django.contrib import admin
# Register your models here.

from .models import YazilarTabloAdiKlasi

class YazilarAdmin(admin.ModelAdmin):
    list_display=['baslik','yayinlanma_tarihi', 'slug_alani_modelden']
    list_display_links=['yayinlanma_tarihi']
    list_filter=['yayinlanma_tarihi', 'yazar_modelden']
    search_fields=['baslik','metin']
    list_editable=['baslik']

    #prepopulated_fields={'slug_alani_modelden':('baslik',)}

    class Meta:
        model=YazilarTabloAdiKlasi

admin.site.register(YazilarTabloAdiKlasi,YazilarAdmin)
