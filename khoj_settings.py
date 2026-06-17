
import os

# Override database settings to use SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(os.environ.get("KHOJ_DATA_DIR", r"E:\Khoj\data"), "khoj.db"),
    }
}
