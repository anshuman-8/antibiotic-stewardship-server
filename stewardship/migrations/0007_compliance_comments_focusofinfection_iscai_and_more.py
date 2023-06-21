# Generated by Django 4.1.5 on 2023-06-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stewardship", "0006_alter_patient_admittingdoctor_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="compliance",
            name="comments",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="focusofinfection",
            name="isCAI",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="focusofinfection",
            name="isHAI",
            field=models.BooleanField(default=False),
        ),
    ]