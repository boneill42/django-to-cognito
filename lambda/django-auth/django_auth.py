from django.contrib.auth import hashers
from django.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.databases.mysql import MySQLDialect
from sqlalchemy.sql import text

# ------------------------------------------------------------------------------------------
# Database
# ------------------------------------------------------------------------------------------
dialect = MySQLDialect()

engine_defaults = {
    'pool_size': 4,
    'max_overflow': 0,
    'pool_recycle': 300,
    'pool_timeout': 30.0,
}

OPTIONS = {
    'charset': 'utf8',
    'use_unicode': True,
}


def none_if_empty(s):
    return s if s else None


def make_dsn(db_settings):
    return str(URL(
        'mysql',
        none_if_empty(db_settings['USER']),
        none_if_empty(db_settings['PASSWORD']),
        none_if_empty(db_settings['HOST']),
        none_if_empty(db_settings['PORT']),
        none_if_empty(db_settings['NAME']),
        OPTIONS))


QUERY_PASSWORD_BY_USER = text(
    "SELECT password "
    "FROM auth_user "
    "WHERE username = :username"
).compile(dialect=dialect)

# ------------------------------------------------------------------------------------------
# Authentication
# ------------------------------------------------------------------------------------------

dsn = make_dsn(settings.DATABASES['default'])
engine = create_engine(dsn, **engine_defaults)
result = engine.execute(QUERY_PASSWORD_BY_USER, username='boneill@monetate.com')
pw = result.fetchone()['password']
authenticated = hashers.check_password('testpw00', str(pw))
print ("Authenticated: [{}]".format(authenticated))
