import os
import sys
from whitenoise import WhiteNoise


# Path to the folder containing manage.py
project_home = '/home/ggourab2004/WELLNESS'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Set the settings module to point to your actual settings.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'wellness.settings'

# Activate your virtualenv if you are using one (adjust path if needed)
# activate_this = '/home/ggourab2004/.virtualenvs/your-venv/bin/activate_this.py'
# exec(open(activate_this).read(), dict(__file__=activate_this))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
application = WhiteNoise(application)