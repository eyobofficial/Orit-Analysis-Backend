# Generated by Django 2.1.7 on 2019-03-22 03:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=120)),
                ('long_name', models.CharField(help_text='Company official full name.', max_length=255)),
                ('address', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConstructionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('order', models.IntegerField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Construction Category',
                'verbose_name_plural': 'Construction Categories',
            },
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=120)),
                ('long_name', models.CharField(help_text='Company official full name.', max_length=255)),
                ('address', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('short_name', models.CharField(max_length=120)),
                ('long_name', models.CharField(help_text='Company official full name.', max_length=255)),
                ('address', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
