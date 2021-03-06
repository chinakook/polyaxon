from polyaxon.config_manager import config

email_from = config.get_string('POLYAXON_EMAIL_FROM')
email_host = config.get_string('POLYAXON_EMAIL_HOST')
email_port = config.get_int('POLYAXON_EMAIL_PORT')
email_host_user = config.get_string('POLYAXON_EMAIL_HOST_USER', is_optional=True)
email_host_password = config.get_string('POLYAXON_EMAIL_HOST_PASSWORD',
                                        is_optional=True,
                                        is_secret=True)
EMAIL_BACKEND = config.get_string('POLYAXON_EMAIL_BACKEND',
                                  is_optional=True,
                                  default='django.core.mail.backends.console.EmailBackend')
