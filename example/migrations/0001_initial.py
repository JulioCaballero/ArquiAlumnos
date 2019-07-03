# Generated by Django 2.2.1 on 2019-06-28 21:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('year', models.IntegerField()),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Example',
            },
        ),
        migrations.CreateModel(
            name='Example2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('year', models.IntegerField()),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Example2',
            },
        ),
    ]
