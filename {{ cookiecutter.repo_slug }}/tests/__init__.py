{% if cookiecutter.django_module %}
import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.django.settings")

django.setup()
{% endif %}
