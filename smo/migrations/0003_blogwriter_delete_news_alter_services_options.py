# Generated by Django 5.0.4 on 2024-04-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smo', '0002_news_is_published_services_image_alter_news_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogWriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='Slug')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('date_of_creation', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('view_count', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'Запись блога',
                'verbose_name_plural': 'Записи блога',
            },
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]
