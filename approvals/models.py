from django.db import models
from approvals.signals import article_approved
import logging
logr = logging.getLogger(__name__)
# Create your models here.
class Approval(models.Model):
    approved = models.BooleanField(default=False)
    article_id = models.IntegerField()

    def save(self, **kwargs):
        if self.pk is not None and self.approved == True:
            rec = article_approved.send(self, article_id=self.article_id)
            logr.debug("Approved article")
        super(Approval, self).save(**kwargs)
