from django.contrib import admin
from .models import PatternType, PatternCompany, Pattern, PatternView, Project


class ProjectInline(admin.TabularInline):
    model = Project


@admin.register(PatternView)
class PatternViewAdmin(admin.ModelAdmin):
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('owner', 'pattern', 'start_date', 'finish_date')
    fields = ['owner', 'pattern', 'fabric', ('start_date', 'finish_date'), 'notes']


# Register your models here.
admin.site.register(PatternType)
admin.site.register(PatternCompany)
admin.site.register(Pattern)
