# Generated by Django 4.0.4 on 2022-04-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]