# Generated by Django 2.1.3 on 2018-12-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Firstyear', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chemsemsubject',
            name='imagelink',
        ),
        migrations.AddField(
            model_name='chemsemsubject',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]