from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

# class SuitConfig(DjangoSuitConfig):
#     layout='vertical'