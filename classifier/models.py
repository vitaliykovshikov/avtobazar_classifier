#encoding: utf-8
import simplejson
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _
from django.conf import settings

from classifier import settings as classifier_settings


class Lng(models.Model):
    """
    Lang versions
    """
    lng = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        pass


class Params(models.Model):
    """
    Params table for classifiers
    """
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        pass


class Values(models.Model):
    """
    Values of Params for classifiers
    """
    params = models.ForeignKey(Params)
    classifier = models.ForeignKey('Classifier', related_name='values_classifier')
    lng = models.ForeignKey(Lng, null=True, blank=True)
    value_int = models.IntegerField(null=True, blank=True)
    value_timestamp = models.DateTimeField(null=True, blank=True)
    value_float = models.FloatField(null=True, blank=True)
    value_varchar = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return '%s%s%s%s' % (
            self.value_int, self.value_timestamp,
            self.value_float, self.value_varchar
        )


# class MPTTPropertiesMixin(object):
#
#     @property
#     def level(self):
#         return self.lvl
#
#     @property
#     def lft(self):
#         return self.ltk
#
#     @property
#     def rght(self):
#         return self.rtk

class Classifier(MPTTModel):
    translit = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    sort = models.IntegerField()
    status = models.IntegerField()

    classifiers = models.ManyToManyField('self', blank=True)

    #deprecated
    decomposition_data = models.CharField(max_length=4000)

    class Meta:
        ordering = ['-sort', 'translit']
        verbose_name_plural = _(u'Классификатор')

    class MPTTMeta:
        left_attr = 'ltk'
        right_attr = 'rtk'
        tree_id_attr = 'tree_id'
        level_attr = 'lvl'

    def __unicode__(self):
        return self.translit

    def get_children(self, **kwargs):
        """
        Return children. Can use related param for return related children.
        :param kwargs: related - takes list of related types 'car', 'bus', etc
        :return: QuerySet
        """
        qs = super(Classifier, self).get_children()
        if 'related' in kwargs and isinstance(kwargs['related'], list):
            qs = qs.filter(classifiers__translit__in=kwargs['related'])
        return qs

    def __getattr__(self, name):
        """
        Custom getattr method for return attributes witch saved in decomposition_data
        :param name: - name of the param
        :return:
        """
        if name in classifier_settings.GETATTR_CHOICES:
            if self.decomposition_data:
                for key, i in simplejson.loads(self.decomposition_data).items():
                    if key == name:
                        if name in ['title', 'meta_title', 'declination', 'alternative_title']:
                            try:
                                return i[get_language()]
                            except KeyError:
                                try:
                                    return i[settings.LANGUAGE_CODE]
                                except KeyError:
                                    pass
                        for k, v in i.items():
                            if k == self.get_lng() or k == 'None':
                                return v
                if name == 'title':
                    return self.translit
                else:
                    return None
        raise AttributeError(name)
