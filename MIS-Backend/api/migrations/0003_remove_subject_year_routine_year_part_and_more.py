# Generated by Django 4.2.4 on 2023-12-23 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_teacher_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='year',
        ),
        migrations.AddField(
            model_name='routine',
            name='year_part',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
