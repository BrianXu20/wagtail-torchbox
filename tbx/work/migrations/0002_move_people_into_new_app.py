# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-18 16:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0001_initial"),
        ("people", "0001_initial"),
        ("torchbox", "0112_move_people_into_new_app"),
    ]

    run_before = [
        ("torchbox", "0113_move_people_into_new_app_2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workpageauthor",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="people.PersonPage",
            ),
        ),
    ]
