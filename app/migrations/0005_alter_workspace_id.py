# Generated by Django 5.0.1 on 2024-03-03 13:18

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_note_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
