# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-15 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import tbx.core.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailmarkdown.blocks

from tbx.core.utils.migrations import for_each_page_revision


def update_contenttypes(apps, schema_editor):
    Page = apps.get_model("wagtailcore.Page")
    ContentType = apps.get_model("contenttypes.ContentType")

    blog_index_prev, created = ContentType.objects.get_or_create(
        app_label="torchbox", model="blogindexpage"
    )
    blog_index_next, created = ContentType.objects.get_or_create(
        app_label="blog", model="blogindexpage"
    )
    blog_page_prev, created = ContentType.objects.get_or_create(
        app_label="torchbox", model="blogpage"
    )
    blog_page_next, created = ContentType.objects.get_or_create(
        app_label="blog", model="blogpage"
    )

    Page.objects.filter(content_type=blog_index_prev).update(
        content_type=blog_index_next
    )
    Page.objects.filter(content_type=blog_page_prev).update(content_type=blog_page_next)

    blog_index_prev.delete()
    blog_page_prev.delete()


def reverse_update_contenttypes(apps, schema_editor):
    Page = apps.get_model("wagtailcore.Page")
    ContentType = apps.get_model("contenttypes.ContentType")

    blog_index_prev, created = ContentType.objects.get_or_create(
        app_label="torchbox", model="blogindexpage"
    )
    blog_index_next, created = ContentType.objects.get_or_create(
        app_label="blog", model="blogindexpage"
    )
    blog_page_prev, created = ContentType.objects.get_or_create(
        app_label="torchbox", model="blogpage"
    )
    blog_page_next, created = ContentType.objects.get_or_create(
        app_label="blog", model="blogpage"
    )

    Page.objects.filter(content_type=blog_index_next).update(
        content_type=blog_index_prev
    )
    Page.objects.filter(content_type=blog_page_next).update(content_type=blog_page_prev)

    blog_index_next.delete()
    blog_page_next.delete()


# Update the content types in revisions or django-modelcluster will crash when trying to deserialise
@for_each_page_revision("blog.BlogIndexPage", "blog.BlogPage")
def update_content_type_in_revisions(page, revision_content):
    revision_content["content_type"] = page.content_type_id
    return revision_content


def nooperation(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtaildocs", "0008_document_file_size"),
        ("torchbox", "0109_move_blog_into_new_app"),
        ("wagtailcore", "0040_page_draft_title"),
    ]

    run_before = [
        ("torchbox", "0110_rename_blogpagetaglist_to_tag"),
    ]

    state_operations = [
        migrations.CreateModel(
            name="BlogIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                ("intro", models.TextField(blank=True)),
                ("show_in_play_menu", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogIndexPageRelatedLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "link_external",
                    models.URLField(blank=True, verbose_name="External link"),
                ),
                ("title", models.CharField(help_text="Link title", max_length=255)),
                (
                    "link_document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtaildocs.Document",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="BlogPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "intro",
                    wagtail.core.fields.RichTextField(
                        blank=True,
                        verbose_name="Intro (used for blog index and Planet Drupal listings)",
                    ),
                ),
                (
                    "body",
                    wagtail.core.fields.RichTextField(
                        blank=True,
                        verbose_name="body (deprecated. Use streamfield instead)",
                    ),
                ),
                (
                    "colour",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("orange", "Orange"),
                            ("blue", "Blue"),
                            ("white", "White"),
                        ],
                        max_length=255,
                        verbose_name="Listing card colour if left blank will display image",
                    ),
                ),
                (
                    "streamfield",
                    wagtail.core.fields.StreamField(
                        [
                            (
                                "h2",
                                wagtail.core.blocks.CharBlock(
                                    classname="title", icon="title"
                                ),
                            ),
                            (
                                "h3",
                                wagtail.core.blocks.CharBlock(
                                    classname="title", icon="title"
                                ),
                            ),
                            (
                                "h4",
                                wagtail.core.blocks.CharBlock(
                                    classname="title", icon="title"
                                ),
                            ),
                            (
                                "intro",
                                wagtail.core.blocks.RichTextBlock(icon="pilcrow"),
                            ),
                            (
                                "paragraph",
                                wagtail.core.blocks.RichTextBlock(icon="pilcrow"),
                            ),
                            (
                                "aligned_image",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "alignment",
                                            tbx.core.blocks.ImageFormatChoiceBlock(),
                                        ),
                                        ("caption", wagtail.core.blocks.CharBlock()),
                                        (
                                            "attribution",
                                            wagtail.core.blocks.CharBlock(
                                                required=False
                                            ),
                                        ),
                                    ],
                                    label="Aligned image",
                                ),
                            ),
                            (
                                "wide_image",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        )
                                    ],
                                    label="Wide image",
                                ),
                            ),
                            (
                                "bustout",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        ("text", wagtail.core.blocks.RichTextBlock()),
                                    ]
                                ),
                            ),
                            (
                                "pullquote",
                                wagtail.core.blocks.StructBlock(
                                    [
                                        (
                                            "quote",
                                            wagtail.core.blocks.CharBlock(
                                                classname="quote title"
                                            ),
                                        ),
                                        (
                                            "attribution",
                                            wagtail.core.blocks.CharBlock(),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "raw_html",
                                wagtail.core.blocks.RawHTMLBlock(
                                    icon="code", label="Raw HTML"
                                ),
                            ),
                            ("embed", wagtail.embeds.blocks.EmbedBlock(icon="code")),
                            (
                                "markdown",
                                wagtailmarkdown.blocks.MarkdownBlock(icon="code"),
                            ),
                        ]
                    ),
                ),
                (
                    "author_left",
                    models.CharField(
                        blank=True,
                        help_text="author who has left Torchbox",
                        max_length=255,
                    ),
                ),
                ("date", models.DateField(verbose_name="Post date")),
                (
                    "marketing_only",
                    models.BooleanField(
                        default=False,
                        help_text="Display this blog post only on marketing landing page",
                    ),
                ),
                ("canonical_url", models.URLField(blank=True, max_length=255)),
                (
                    "feed_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="torchbox.TorchboxImage",
                    ),
                ),
            ],
            options={"abstract": False,},
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogPageAuthor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="torchbox.PersonPage",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_author",
                        to="blog.BlogPage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="BlogPageRelatedLink",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "link_external",
                    models.URLField(blank=True, verbose_name="External link"),
                ),
                ("title", models.CharField(help_text="Link title", max_length=255)),
                (
                    "link_document",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtaildocs.Document",
                    ),
                ),
                (
                    "link_page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="related_links",
                        to="blog.BlogPage",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.CreateModel(
            name="BlogPageTagSelect",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags",
                        to="blog.BlogPage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_page_tag_select",
                        to="torchbox.BlogPageTagList",
                    ),
                ),
            ],
            options={"ordering": ["sort_order"], "abstract": False,},
        ),
        migrations.AddField(
            model_name="blogindexpagerelatedlink",
            name="link_page",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="wagtailcore.Page",
            ),
        ),
        migrations.AddField(
            model_name="blogindexpagerelatedlink",
            name="page",
            field=modelcluster.fields.ParentalKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="related_links",
                to="blog.BlogIndexPage",
            ),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations, database_operations=[],
        ),
        migrations.SeparateDatabaseAndState(
            state_operations=[],
            database_operations=[
                migrations.RunPython(nooperation, update_content_type_in_revisions),
                migrations.RunPython(update_contenttypes, reverse_update_contenttypes),
                migrations.RunPython(update_content_type_in_revisions, nooperation),
            ],
        ),
    ]
