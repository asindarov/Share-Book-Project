# Generated by Django 3.2.12 on 2022-03-17 16:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0007_book_state_of_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='UserBook',
        ),
    ]