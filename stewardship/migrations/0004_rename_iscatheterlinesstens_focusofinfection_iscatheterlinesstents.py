# Generated by Django 4.1.5 on 2023-02-28 10:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "stewardship",
            "0003_rename_iscatheterlinesstents_focusofinfection_iscatheterlinesstens",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="focusofinfection",
            old_name="isCatheterLinesStens",
            new_name="isCatheterLinesStents",
        ),
    ]
