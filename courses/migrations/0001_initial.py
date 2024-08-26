# Generated by Django 5.1 on 2024-08-26 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('course_code', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('instance_id', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='courses.course')),
            ],
        ),
    ]
