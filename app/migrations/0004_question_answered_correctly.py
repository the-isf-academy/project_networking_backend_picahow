# Generated by Django 5.1.2 on 2024-10-15 07:46

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_question_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answered_correctly',
            field=banjo.models.BooleanField(default=False),
        ),
    ]
