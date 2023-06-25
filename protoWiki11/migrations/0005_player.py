# Generated by Django 4.2 on 2023-06-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protoWiki11', '0004_weapon_location_weapon_skill_alter_item_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=5)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
