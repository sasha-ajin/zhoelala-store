# Generated by Django 3.1.6 on 2021-04-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210425_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(null=True, to='store.Sizes'),
        ),
    ]
