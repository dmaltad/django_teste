from django.contrib import admin
from .models import CA, EPI, Estoque, Colaborador, Entrega

admin.site.register(CA)
admin.site.register(EPI)
admin.site.register(Estoque)
admin.site.register(Colaborador)
admin.site.register(Entrega)