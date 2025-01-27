#
#
# from django.contrib.sessions.base_session import (
#     AbstractBaseSession, BaseSessionManager,
# )
#
#
# class SessionManager(BaseSessionManager):
#     use_in_migrations = True
#
#
# class Session(AbstractBaseSession):
#
#     objects = SessionManager()
#
#     @classmethod
#     def get_session_store_class(cls):
#         from django.contrib.sessions.backends.db import SessionStore
#         return SessionStore
#
#     class Meta(AbstractBaseSession.Meta):
#         db_table = 'django_session'

from django.contrib.sessions.backends.base import SessionBase


class SessionStore(SessionBase):
    pass
