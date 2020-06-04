from django.core.exceptions import ValidationError
from django.db import models


LAYOUT_CHOICES = (
    ('standard', 'Standard'),
    ('stacked', 'Stacked'),
)

def layout_validator(value):
    if value[0] != "#":
        raise ValidationError("Must start with #")
    if len(value) == 4 or len(value)==7:
        return value
    raise ValidationError("Incorrect Length")

class Page(models.Model):
    title                       = models.CharField(max_length=220)
    title_description           = models.TextField(blank=True, null=True)
    title_button                = models.CharField(max_length=50, default="Join")
    title_btn_url               = models.CharField(max_length=50, blank=True, null=True)
    content                     = models.TextField(blank=True, null=True)
    show_nav                    = models.BooleanField(default=True)
    nav_color                   = models.CharField(max_length=7, default='#000000', validators=[layout_validator])

    def __str__(self):
        return self.title