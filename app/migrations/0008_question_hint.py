# Generated by Django 5.1.2 on 2024-10-24 04:58

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_question_hint'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hint',
            field=banjo.models.StringField(default=''),
        ),
    ]
