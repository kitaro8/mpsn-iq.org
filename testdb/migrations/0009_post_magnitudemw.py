# Generated by Django 5.0.3 on 2024-06-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0008_remove_post_magnitudemw'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='MagnitudeMW',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
