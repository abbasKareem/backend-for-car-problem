# Generated by Django 4.1.6 on 2023-02-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_remove_carproblemlocation_car_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartype",
            name="photo",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="image_2",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="image_3",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="image_4",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="image_5",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="main_image",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
