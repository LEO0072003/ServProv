# Generated by Django 4.0.5 on 2022-10-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_ph_no_customersmodel_phone_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersmodel',
            name='tell_us_about_your_business',
            field=models.TextField(max_length=2000),
        ),
    ]
