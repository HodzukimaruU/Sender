DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB_SENDER'],  # type: ignore
        'HOST': os.environ['POSTGRES_HOST'],  # type: ignore
        'PORT': os.environ['POSTGRES_PORT'],  # type: ignore
        'USER': os.environ['POSTGRES_USER_SENDER'],  # type: ignore
        'PASSWORD': os.environ['POSTGRES_PASSWORD_SENDER'],  # type: ignore
        'ATOMIC_REQUESTS': True,
    }
}
# POSTGRES_HOST = 'postgres'
# POSTGRES_PORT = 5432
# POSTGRES_PASSWORD = 'postgres'

# POSTGRES_DB_SENDER = 'sender_api'
# POSTGRES_USER_SENDER = 'uppa'
# POSTGRES_PASSWORD_SENDER = '3355110k17'

# DATABASES = {
#     'default': {
#         'OPTIONS': {
#             'options': f'-c search_path={os.environ.get("POSTGRES_SCHEMA_BOT")}'  # type: ignore
#         },
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('POSTGRES_DB_BOT'),  # type: ignore
#         'USER': os.environ.get('POSTGRES_USER_BOT'),  # type: ignore
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD_BOT'),  # type: ignore
#         'HOST': os.environ.get('POSTGRES_HOST'),  # type: ignore
#         'PORT': os.environ.get('POSTGRES_PORT'),  # type: ignore
#     }
# }
