# Generated by Django 3.0.4 on 2020-04-02 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0002_auto_20200402_0835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ('name',)},
        ),
    ]
