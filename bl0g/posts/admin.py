from typing import Any
from django.contrib import admin
from django.contrib.admin.widgets import AdminTextareaWidget
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from posts.models import Post


class AdminTextAreaPaste(AdminTextareaWidget):
    class Media:
        js = [
            'paste.js',
        ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }
    list_display = (
        'title',
        'stamp',
        'author',
    )
    exclude = (
        'brief_html',
        'text_html',
    )
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminPagedownWidget },
    # }
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminTextAreaPaste },
    #     # models.TextField: {'widget': AdminMartorWidget},
    # }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return super().get_queryset(request).filter(author=request.user)
    # def save_model(self, request, obj, form, change):
    #     if not obj.id:
    #         if not obj.author:
    #             obj.author = request.user
    #     return super().save_model(request, obj, form, change)
