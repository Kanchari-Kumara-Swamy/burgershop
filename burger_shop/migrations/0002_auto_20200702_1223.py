# Generated by Django 3.0.6 on 2020-07-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burgermodel',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='phoneno',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='userid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='ordereditems',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='phoneno',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
