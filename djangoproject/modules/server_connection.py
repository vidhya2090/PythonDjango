from django.http import HttpResponse
from sqlalchemy import create_engine
import pandas as pd
from django.conf import settings


def mysql_connection():
    user = settings.DATABASES['default1']['USER']
    password = settings.DATABASES['default1']['PASSWORD']
    database_name = settings.DATABASES['default1']['NAME']

    database_url = 'mysql://{user}:{password}@localhost:3306/{database_name}'.format(
        user=user,
        password=password,
        database_name=database_name,
    )

    engine = create_engine(database_url, echo=False)
    return engine