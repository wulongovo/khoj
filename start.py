
import os, sys

# Disable all proxies and set HF offline
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("http_proxy", None)
os.environ.pop("https_proxy", None)
os.environ.pop("ALL_PROXY", None)
os.environ.pop("all_proxy", None)
os.environ["NO_PROXY"] = "*"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

sys.path = [p for p in sys.path if 'hermes_env' not in p and p.strip() != '']

os.environ["KHOJ_DATA_DIR"] = r"E:\Khoj\data"
os.environ["DJANGO_SETTINGS_MODULE"] = "khoj.app.settings"
os.environ["POSTGRES_HOST"] = "localhost"
os.environ["POSTGRES_PORT"] = "5432"
os.environ["POSTGRES_DB"] = "khoj"
os.environ["POSTGRES_USER"] = "khoj"
os.environ["POSTGRES_PASSWORD"] = "khoj_pass_2026"
os.environ["KHOJ_ADMIN_EMAIL"] = "admin@khoj.local"
os.environ["KHOJ_ADMIN_PASSWORD"] = "khoj2026"

os.makedirs(r"E:\Khoj\data", exist_ok=True)

import khoj.app.settings as ks
ks.TIME_ZONE = "GMT"
ks.USE_TZ = False
ks.DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "PORT": "5432",
        "USER": "khoj",
        "NAME": "khoj",
        "PASSWORD": "khoj_pass_2026",
        "CONN_MAX_AGE": 0,
        "CONN_HEALTH_CHECKS": True,
    }
}

sys.argv = ["khoj", "--anonymous-mode", "--non-interactive"]

import django
django.setup()
from django import db
db.connections.close_all()

print("Starting Khoj at http://localhost:42110 (anonymous, non-interactive, offline)")
from khoj.main import run
run()
