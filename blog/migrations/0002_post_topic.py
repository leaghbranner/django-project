# Generated by Django 3.2.8 on 2022-02-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(default='', max_length=100),
        ),
    ]