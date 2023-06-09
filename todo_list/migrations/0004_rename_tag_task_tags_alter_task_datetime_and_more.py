# Generated by Django 4.1 on 2023-03-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo_list", "0003_alter_task_datetime"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="tag",
            new_name="tags",
        ),
        migrations.AlterField(
            model_name="task",
            name="datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="is_done",
            field=models.BooleanField(default=False),
        ),
    ]
