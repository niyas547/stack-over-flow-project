# Generated by Django 4.1.2 on 2022-10-26 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
