# Generated by Django 2.1.7 on 2019-03-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructioncategory',
            name='icon',
            field=models.CharField(max_length=120),
            preserve_default=False,
        ),
    ]
