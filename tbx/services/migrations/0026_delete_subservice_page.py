# Generated by Django 2.1.5 on 2019-03-21 23:59

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailforms", "0003_capitalizeverbose"),
        ("torchbox", "0125_auto_20190216_1713"),
        ("wagtailsearchpromotions", "0002_capitalizeverbose"),
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
        ("people", "0014_contactreasonslist_is_default_not_unique"),
        ("wagtailredirects", "0006_redirect_increase_max_length"),
        ("services", "0025_servicepage_theme"),
    ]

    operations = [
        migrations.RemoveField(model_name="subservicepage", name="parent_service",),
        migrations.RemoveField(model_name="subservicepage", name="servicepage_ptr",),
        migrations.DeleteModel(name="SubServicePage",),
    ]
