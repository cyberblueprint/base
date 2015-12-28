
from django.contrib import admin

from .models import Empresa, Licencia


# Register your models here.
class EmpresaAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ['nombre']

class LicenciaAdmin(admin.ModelAdmin):
	date_hierarchy = 'inicio'
	search_fields = ['inicio', 'fin']
	list_display = ['usuario', 'numero_de_monitores', 'numero_de_pasos', 'token', 'inicio', 'fin', 'habilitado', 'producto']
	list_filter = ['numero_de_monitores', 'habilitado']
	#list_editable = ['habilitado']
	exclude = ('usuario',)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		obj.save()

	def mostrar_empresa(self, obj):
		return "\n".join([a.empresa for a in obj.empresa.all()])


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Licencia, LicenciaAdmin)