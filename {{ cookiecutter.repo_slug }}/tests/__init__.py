{% if cookiecutter.django_module %}import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.project.settings")

django.setup(){% endif %}
