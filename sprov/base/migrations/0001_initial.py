# Generated by Django 4.0.5 on 2022-10-01 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_name', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=400)),
            ],
        ),
    ]