# Generated by Django 3.0.4 on 2020-07-02 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_articles_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='desc',
        ),
    ]
