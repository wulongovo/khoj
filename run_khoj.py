
import os, sys

# Set environment
os.environ["KHOJ_DATA_DIR"] = r"E:\Khoj\data"

# Patch Django settings to use SQLite before khoj loads
import django.conf
original_settings = django.conf.settings

# Monkey-patch the database configuration
import khoj.app.settings as khoj_settings
khoj_settings.DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(r"E:\Khoj\data", "khoj.db"),
    }
}

# Now run khoj
from khoj.main import main
main()
