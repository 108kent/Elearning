# Generated by Django 3.2.19 on 2023-06-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
        ('module', '0003_module_quizzes'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='assignments',
            field=models.ManyToManyField(to='assignment.Assignment'),
        ),
    ]
