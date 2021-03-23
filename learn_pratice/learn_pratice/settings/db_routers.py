
from django.conf import settings

DATABASE_MAPPING = settings.DATABASE_APPS_MAPPING


class AppsRouter(object):

    def db_for_read(self, model, **hints):
        '''建议 model 对象读操作时使用的数据库'''
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return 'default'


    def db_for_write(self, model, **hints):
        '''建议 model 对象写操作时使用的数据库'''
        if model._meta.app_label in DATABASE_MAPPING:
            return DATABASE_MAPPING[model._meta.app_label]
        return 'default'


    def allow_relation(self, obj1, obj2, **hints):
        '''当 obj1 和 obj2 之间允许有关系时返回 True ，不允许时返回 False ，或者没有 意见时返回 None'''
        db_obj1 = DATABASE_MAPPING.get(obj1._meta.app_label)
        db_obj2 = DATABASE_MAPPING.get(obj2._meta.app_label)
        if db_obj1 and db_obj2:
            if db_obj1 == db_obj2:
                return True
            else:
                return False
        return None


    def allow_syncdb(self, db, model):
        '''决定 model 是否可以和 db 为别名的数据库同步'''
        '''True就是可以，False就是拒绝，None是不管'''
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(model._meta.app_label) == db
        elif model._meta.app_label in DATABASE_MAPPING:
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print(db, app_label, model_name, hints)
        if db in DATABASE_MAPPING.values():
            return DATABASE_MAPPING.get(app_label) == db
        elif app_label in DATABASE_MAPPING:
            return False
        return None


class MongoRouter(object):
    pass