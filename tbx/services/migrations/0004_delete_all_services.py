# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-21 16:53
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations


def delete_all_services(apps, schema_editor):
    Page = apps.get_model('wagtailcore.Page')
    ContentType = apps.get_model('contenttypes.ContentType')

    service_index_ct = ContentType.objects.get(app_label='services', model='serviceindexpage')
    service_page_ct = ContentType.objects.get(app_label='services', model='servicepage')

    # Dangerously delete existing service pages
    Page.objects.filter(content_type__in=[service_index_ct, service_page_ct]).delete()

    # Fix the tree
    call_command('fixtree')


def nooperation(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_servicepage_service'),
    ]

    operations = [
        migrations.RunPython(delete_all_services, nooperation),
    ]
