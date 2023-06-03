# Generated by Django 3.2.19 on 2023-06-02 15:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]