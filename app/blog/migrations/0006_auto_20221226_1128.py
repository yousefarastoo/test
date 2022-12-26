# Generated by Django 2.2 on 2022-12-26 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='نویسندگان', to=settings.AUTH_USER_MODEL, verbose_name='نویسندگان'),
        ),
    ]
