# Generated by Django 4.1.3 on 2023-04-01 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_create_data_article_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
    ]
