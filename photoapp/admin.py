from django.contrib import admin
from .models import PhotoRepo


class PhotoRepoAdmin(admin.ModelAdmin):
    list_display = ('title', 'profile', 'created_date', 'updated_date')
    list_filter = ('title',)


admin.site.register(PhotoRepo)
