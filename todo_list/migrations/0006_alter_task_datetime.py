# Generated by Django 4.1 on 2023-03-15 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("todo_list", "0005_alter_task_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="datetime",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
