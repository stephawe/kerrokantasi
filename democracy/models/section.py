from django.db import models
from django.utils.translation import ugettext_lazy as _
from enumfields.fields import EnumField
from reversion import revisions

from democracy.enums import SectionType
from democracy.models.comment import BaseComment, recache_on_save
from democracy.models.images import BaseImage

from .base import ORDERING_HELP, Commentable, StringIdBaseModel
from .hearing import Hearing


class Section(Commentable, StringIdBaseModel):
    hearing = models.ForeignKey(Hearing, related_name='sections', on_delete=models.PROTECT)
    ordering = models.IntegerField(verbose_name=_('ordering'), default=1, db_index=True, help_text=ORDERING_HELP)
    type = EnumField(verbose_name=_('type'), enum=SectionType, default=SectionType.PLAIN)
    title = models.CharField(verbose_name=_('title'), max_length=255, blank=True)
    abstract = models.TextField(verbose_name=_('abstract'), blank=True)
    content = models.TextField(verbose_name=_('content'), blank=True)

    class Meta:
        ordering = ["ordering"]
        verbose_name = _('section')
        verbose_name_plural = _('sections')

    def __str__(self):
        return "%s: %s" % (self.hearing, self.title)

    def save(self, *args, **kwargs):
        if not self.pk and self.ordering == 1 and self.hearing_id:
            # Automatically derive next ordering on initial save, if possible
            self.ordering = max(self.hearing.sections.values_list("ordering", flat=True) or [0]) + 1
        return super(Section, self).save(*args, **kwargs)

    def check_commenting(self, request):
        super().check_commenting(request)
        self.hearing.check_commenting(request)


class SectionImage(BaseImage):
    parent_field = "section"
    section = models.ForeignKey(Section, related_name="images")

    class Meta:
        verbose_name = _('section image')
        verbose_name_plural = _('section images')


@revisions.register
@recache_on_save
class SectionComment(BaseComment):
    parent_field = "section"
    parent_model = Section
    section = models.ForeignKey(Section, related_name="comments")

    class Meta:
        verbose_name = _('section comment')
        verbose_name_plural = _('section comments')