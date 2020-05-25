from django.contrib import admin
from django.db import models
from django.contrib.admin.widgets import AdminTextareaWidget
from posts.models import Post
# from pagedown.widgets import AdminPagedownWidget

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
    formfield_overrides = {
        models.TextField: {'widget': AdminTextAreaPaste },
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # def save_model(self, request, obj, form, change):
    #     if not obj.id:
    #         if not obj.author:
    #             obj.author = request.user
    #     return super().save_model(request, obj, form, change)
