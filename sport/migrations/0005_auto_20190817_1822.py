# Generated by Django 2.2.4 on 2019-08-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_auto_20190817_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Reserved'), ('2', 'Available')], default='A', max_length=1),
        ),
    ]