# Generated by Django 3.2.19 on 2023-06-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
        ('classroom', '0004_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='questions',
            field=models.ManyToManyField(to='question.Question'),
        ),
    ]
