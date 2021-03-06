# Generated by Django 3.0.6 on 2020-06-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='layout',
            field=models.CharField(choices=[('standard', 'Standard'), ('stacked', 'Stacked')], default='standard', max_length=20),
        ),
        migrations.AddField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AddField(
            model_name='page',
            name='show_nav',
            field=models.BooleanField(default=True),
        ),
    ]
