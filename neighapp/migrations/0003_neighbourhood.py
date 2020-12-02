# Generated by Django 3.1.3 on 2020-12-02 06:48

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neighapp', '0002_auto_20201202_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('hoodLogo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('definition', models.TextField()),
                ('occupants', models.IntegerField(blank=True, null=True)),
                ('emergencyNo', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhood', to='neighapp.adminprofile')),
            ],
            options={
                'db_table': 'neighborhood',
            },
        ),
    ]
