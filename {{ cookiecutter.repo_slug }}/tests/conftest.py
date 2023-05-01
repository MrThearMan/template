{% if cookiecutter.django_module %}
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.django.settings")
{% endif %}
