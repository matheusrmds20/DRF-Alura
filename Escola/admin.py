from django.contrib import admin
from Escola.models import estudante, curso, matricula

class estudantes(admin.ModelAdmin):

    list_display = ('id','nome','email','cpf','nascimento','celular')
    list_display_links = ('id','nome')
    list_per_page = 20
    search_fields = ('nome','cpf',)
    ordering = ('nome',)

admin.site.register(estudante, estudantes)


class cursos(admin.ModelAdmin):

    list_display = ('id','codigo','nivel')
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)

admin.site.register(curso, cursos)


class matriculas(admin.ModelAdmin):

    list_display = ('id','estudante','curso','periodo')
    list_display_links = ('id','estudante',)
    


admin.site.register(matricula, matriculas)
    