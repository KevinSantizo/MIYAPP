# Generated by Django 2.2.4 on 2019-08-23 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_remove_team_group_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.Group')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.Team')),
            ],
        ),
    ]
