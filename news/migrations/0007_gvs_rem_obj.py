# Generated by Django 3.2.7 on 2022-03-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20220326_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='gvs',
            name='rem_obj',
            field=models.CharField(default='не указано', max_length=50, verbose_name='ТК,НО, ЦТП'),
        ),
    ]
