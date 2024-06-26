# Generated by Django 5.0.4 on 2024-04-11 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Специализация')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.speciality'),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
