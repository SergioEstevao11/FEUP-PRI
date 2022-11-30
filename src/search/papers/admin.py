from django.contrib import admin

from .models import Paper

class PaperAdmin(admin.ModelAdmin):
    list_display = ("link", "summary", "title", "authors", "date", "areas", "fields", "subjects")

admin.site.register(Paper, PaperAdmin)
# Register your models here.
