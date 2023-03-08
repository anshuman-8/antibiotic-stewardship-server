# Generated by Django 4.1.5 on 2023-03-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("stewardship", "0006_compliance_serum_creatinine"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="analysisform",
            name="drugAdministered",
        ),
        migrations.AddField(
            model_name="analysisform",
            name="drugAdministered",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="stewardship.drugadministeredreview",
            ),
            preserve_default=False,
        ),
    ]
