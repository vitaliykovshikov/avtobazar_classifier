
class ClassifierRouter(object):
    """
    A router that sets up all read operations to `classifier` to
    `classifier` db
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'classifier':
            return 'classifier'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all write operations to the `default`"
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'classifier' or obj2._meta.app_label == 'classifier':
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'default':
            return True
        return False
