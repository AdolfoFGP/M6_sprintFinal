# Generated by Django 4.2.4 on 2023-08-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='tienda/img', default='tienda/img/gato.jpg', null=True),
        ),
    ]
