# Generated by Django 3.2.6 on 2021-09-11 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_contactmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='nama_surname',
            new_name='name_surname',
        ),
    ]
