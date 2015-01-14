from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from feincms.admin.tree_editor import TreeEditor

from classifier.models import Classifier

class ClassifierTreeAdmin(TreeEditor):
    def _actions_column(self, page):
        actions = super(ClassifierTreeAdmin, self)._actions_column(page)
        actions.insert(0, u'<a href="add/?parent=%s" title="%s"><img src="%simg/icon_addlink.gif" alt="%s"></a>' %
                   (page.pk, _(u'Add child classifier'),
                   settings.ADMIN_MEDIA_PREFIX, _(u'Add child classifier')))
        # actions.insert(0, u'<a href="%s" title="%s"><img src="%simg/selector-search.gif" alt="%s" /></a>' %
        #            (page.get_absolute_url(), _(u'View on site'),
        #            settings.ADMIN_MEDIA_PREFIX, _(u'View on site')))
        return actions

admin.site.register(Classifier, ClassifierTreeAdmin)
