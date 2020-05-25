from datetime import datetime
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.utils.html import strip_tags
from filer.fields.image import FilerImageField
# from filer.fields.file import FilerFileField
from .templatetags.md import md
from .templatetags.md import brief

class Post(models.Model):
    cover = FilerImageField(null=True, blank=True, related_name="post_cover", on_delete=models.SET_NULL)
    title = models.CharField("Заголовок", max_length=255)
    slug = models.SlugField("Слаг", max_length=255)
    brief = models.TextField("Кратко", null=True, blank=True)
    brief_html = models.TextField("Кратко", null=True, blank=True)
    text = models.TextField("Текст", null=True, blank=True)
    text_html = models.TextField("Текст", null=True, blank=True)
    author = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)
    stamp = models.DateTimeField('Добавлено', default=datetime.now)
    published = models.BooleanField('Опубликовано', default=False)
    def __str__(self):
        return self.title or 'Публикация без названия'
    class Meta:
        ordering = ['-stamp']
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

@receiver(pre_save, sender=Post)
def render_post(sender, instance, *args, **kwargs):
    if instance.text:
        instance.text_html = md(instance.text)
    if instance.brief:
        instance.brief_html = md(instance.brief)
    else:
        if instance.text:
            instance.brief_html = md(brief(strip_tags(instance.text)))

