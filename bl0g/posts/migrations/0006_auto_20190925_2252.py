# Generated by Django 2.2.5 on 2019-09-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20190904_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='brief_html',
            field=models.TextField(blank=True, null=True, verbose_name='Кратко'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_html',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
