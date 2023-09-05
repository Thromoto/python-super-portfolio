# Generated by Django 4.2.3 on 2023-09-05 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_certifyinginstitution_certificate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="certifying_institution",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.certifyinginstitution",
            ),
        ),
    ]
