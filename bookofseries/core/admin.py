from django.contrib import admin

from bookofseries.core.models import Genre, Author, Catalog, CatalogItem, Language, Comment


class CatalogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class CatalogItemModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'season', 'episodes', 'watched']


class GenreModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ['name']


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name']


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment']


admin.site.register(Genre, GenreModelAdmin)
admin.site.register(Author, AuthorModelAdmin)
admin.site.register(Catalog, CatalogModelAdmin)
admin.site.register(CatalogItem, CatalogItemModelAdmin)
admin.site.register(Language, LanguageModelAdmin)
admin.site.register(Comment, CommentModelAdmin)
