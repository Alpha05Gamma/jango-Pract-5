# Generated by Django 4.2 on 2023-06-07 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protoWiki11', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='runes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
