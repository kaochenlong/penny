# Generated by Django 5.0.4 on 2024-04-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nannies", "0002_nanny_created_at_nanny_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="nanny",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]
