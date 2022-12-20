# Generated by Django 2.2 on 2022-12-20 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(max_length=250, verbose_name='اسلاگ')),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد مقاله'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='description',
            field=models.TextField(verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(max_length=250, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], default='d', max_length=1, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='thumbnail',
            field=models.ImageField(upload_to='images', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=250, verbose_name='عنوان مقاله'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت'),
        ),
        migrations.AddField(
            model_name='articles',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]