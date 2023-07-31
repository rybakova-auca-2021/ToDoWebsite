# Generated by Django 4.2.3 on 2023-07-31 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ToDoApp', '0002_todoitem_user_alter_todoitem_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]