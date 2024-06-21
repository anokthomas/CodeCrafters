from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,PageChooserPanel

class HomePage(Page):
    lead_text=models.CharField(
        max_length=140,
        blank=True,
        help_text='Subheading text undet the banner title',
    )
    botton=models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optimal page to link to',
        on_delete=models.SET_NULL,
    )
    botton_text=models.CharField(
        max_length=140,
        blank=True,
        help_text='Subheading text undet the banner title',
    )
    banner_background_image=models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='The banner backgound image',
        on_delete=models.SET_NULL,
    )
    content_panels=Page.content_panels+ [
        FieldPanel("lead_text"),
        PageChooserPanel("botton"),
        FieldPanel("botton_text"),
        FieldPanel("banner_background_image"),

    ]
