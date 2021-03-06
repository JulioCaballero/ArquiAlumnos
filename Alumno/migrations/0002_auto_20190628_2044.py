# Generated by Django 2.2.1 on 2019-06-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField()),
                ('name', models.CharField(max_length=254)),
                ('lastName', models.CharField(max_length=254)),
                ('matricula', models.CharField(max_length=254)),
                ('career', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'Alumno',
            },
        ),
        migrations.RemoveField(
            model_name='rfid',
            name='id_alumno',
        ),
        migrations.DeleteModel(
            name='Alumnos',
        ),
        migrations.DeleteModel(
            name='Rfid',
        ),
    ]
