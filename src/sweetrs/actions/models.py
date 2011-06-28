from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.contenttypes import generic

ACTION_TYPES = (
    ('product_add', _('Dodanie produktu')),
    ('rating_add', _('Dodanie oceny')),
    ('comment_add', _('Dodanie komentarza')),
)

# Create your models here.
class Action(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    dump = models.CharField(max_length=5000, verbose_name = _("Dump"))

    date = models.DateTimeField(_("Ostatnia zmiana"), auto_now=True)
    user = models.ForeignKey(User)
    type = models.CharField(max_length=50, choices=ACTION_TYPES, verbose_name = _("Typ"))

