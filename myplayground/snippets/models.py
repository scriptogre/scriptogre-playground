from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, TextBlock
from wagtail.fields import StreamField
from wagtail.models import Page


class SnippetIndexPage(Page):
    intro = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("intro", classname="full"),
    ]


class SnippetPage(Page):
    code = models.TextField()
    description = models.TextField()
    body = StreamField(
        [
            ("description", RichTextBlock()),
            ("code", TextBlock(template="snippets/code_block.html")),
        ],
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("code"),
        FieldPanel("body"),
    ]
