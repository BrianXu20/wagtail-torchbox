# Generated by Django 2.1.5 on 2019-02-07 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0016_auto_20190207_1630"),
    ]

    operations = [
        migrations.RenameField(
            model_name="servicepageprocess", old_name="link_page", new_name="page_link",
        ),
        migrations.RenameField(
            model_name="servicepageprocess",
            old_name="link_label",
            new_name="page_link_label",
        ),
    ]
