#encoding: utf-8

from django.core.management.base import BaseCommand
from django.db import connections
from classifier.models import Classifier, Values, Params, Lng

class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    help = 'Migrate classifier to MPTT'

    @staticmethod
    def handle_lng():
        print '====== Start migrate LNG ======'
        for obj in Lng.objects.using('classifier').all():
            lng, created = Lng.objects.using('default').get_or_create(pk=obj.pk, lng=obj.lng, name=obj.name)
            if created:
                print '%s created' % lng
            else:
                print '%s already exists' % lng

    @staticmethod
    def handle_params():
        print '====== Start migrate params ======'
        for obj in Params.objects.using('classifier').all():
            param, created = Params.objects.using('default').get_or_create(pk=obj.pk, type=obj.type, name=obj.name)
            if created:
                print '%s created' % param
            else:
                print '%s already exists' % param

    @staticmethod
    def handle_values():
        print '====== Start migrate values ======'
        for obj in Values.objects.all():
            value, created = Values.objects.using('default').get_or_create(pk=obj.pk, params_id=obj.params_id,
                classifier_id=obj.classifier_id, lng_id=obj.lng_id,
                value_int=obj.value_int, value_timestamp=obj.value_timestamp, value_float=obj.value_float,
                value_varchar=obj.value_varchar)
            if created:
                print '%s created' % value
            else:
                print '%s already exists' % value
        pass

    @staticmethod
    def handle_classifier():
        print '====== Start migrate classifier ======'
        for level in range(6):
            for obj in Classifier.objects.using('classifier').raw('SELECT * FROM classifier_classifier WHERE lvl = %s' % level):
                classifier, created = Classifier.objects.using('default').get_or_create(
                    pk=obj.pk, translit=obj.translit, lvl=obj.lvl, ltk=obj.ltk, parent_id=obj.parent_id, rtk=obj.rtk,
                    sort=obj.sort, status=obj.status, decomposition_data=obj.decomposition_data, tree_id=0)
                if created:
                    print '%s created' % classifier
                else:
                    print '%s already exists' % classifier
            print '-------Finish migrate level %s --------' % level

    @staticmethod
    def handle_classifier_classifiers():
        def dictfetchall(cursor):
            "Returns all rows from a cursor as a dict"
            desc = cursor.description
            return [
                dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()
            ]
        default_cursor = connections['default'].cursor()
        classifier_cursor = connections['classifier'].cursor()
        classifier_cursor.execute('SELECT * FROM classifier_classifier_classifiers');
        for obj in  dictfetchall(classifier_cursor):
            query = "INSERT INTO classifier_classifier_classifiers (to_classifier_id, id, from_classifier_id) VALUES(%s,%s, %s)" % (
                obj['to_classifier_id'], obj['id'], obj['from_classifier_id']
            )
            try:
                default_cursor.execute(query)
            except Exception, e:
                print e
        pass

    def handle(self, *args, **options):
        self.handle_lng()
        self.handle_params()
        self.handle_classifier()
        self.handle_classifier_classifiers()
        self.handle_values()