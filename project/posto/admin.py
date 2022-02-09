from django.contrib import admin
from .models import Tanques, Bombas, Vendas

admin.site.site_header = "postos_abc"

class TanquesAdmin(admin.ModelAdmin):
    list_display = ["id", "conteudo", "volume_m3"]

class BombasAdmin(admin.ModelAdmin):
    list_display = ["id", "referencia", "tanque"]

class VendasAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "litros","valor_abastecido", "valor_de_imposto", "bomba"]

admin.site.register(Tanques, TanquesAdmin)
admin.site.register(Bombas, BombasAdmin)
admin.site.register(Vendas, VendasAdmin)
