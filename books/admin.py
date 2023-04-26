from django.contrib import admin
from books import models

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    list_filter = ["country"]
    search_fields = ["name", "country__name"]


admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Book)
