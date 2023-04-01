# Generated by Django 4.1.3 on 2023-04-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_article_access_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField(default=20)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('0', 'お知らせ'), ('1', '技術'), ('2', 'その他')], max_length=100),
        ),
    ]
