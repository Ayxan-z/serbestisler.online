# Generated by Django 3.2.6 on 2021-09-09 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_categorymodel_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
