# Generated by Django 2.1.3 on 2018-12-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstyear', '0002_auto_20181202_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='chemsemsubject',
            name='link',
            field=models.CharField(default='#', max_length=100),
        ),
        migrations.AddField(
            model_name='physemsubject',
            name='link',
            field=models.CharField(default='#', max_length=100),
        ),
    ]
