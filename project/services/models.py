from django.db import models
from django.forms import ValidationError
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel,PageChooserPanel
class ServiceListingPage(Page):
    # Add fields here, e.g.,
    subtitle = models.TextField(
        blank=True,
        max_length=500,              
    )
    content_panels=Page.content_panels +[FieldPanel('subtitle')]



class ServicePage(Page):
    description = models.TextField(
        blank=True,
        max_length=500,              
    )
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        help_text=u'Select a page to link to this page.',
        on_delete=models.SET_NULL,
    )
    external_page=models.URLField(blank=True)
    botton_text=models.CharField(max_length=100,blank=True) 
    service_image=models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='This image will be used on the Service page',
    )
    content_panels=Page.content_panels +[FieldPanel('description'),PageChooserPanel('internal_page'),FieldPanel('external_page'),FieldPanel('botton_text'),FieldPanel('service_image')]

class ServiceListingPage(Page):
    # Add fields here, e.g.,
    template="services/service_listing_page.html"
    subtitle=models.TextField(blank=True,max_length=500)
    content_panels=Page.content_panels +[FieldPanel('subtitle')]
    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request, *args, **kwargs)
        context['services'] = ServicePage.objects.live().public()
        return context
    def clean(self):
        super().clean()

        if self.internal_page and self.external_page:
            # Both fields are filled out
            raise ValidationError({
                'internal_page': ValidationError("Please only select a page OR enter an external URL"),
                'external_page': ValidationError("Please only select a page OR enter an external URL"),
            })

        if not self.internal_page and not self.external_page:
            raise ValidationError({
                'internal_page': ValidationError("You must always select a page OR enter an external URL"),
                'external_page': ValidationError("You must always select a page OR enter an external URL"),
            })







