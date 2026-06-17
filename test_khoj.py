import os
os.environ["USE_EMBEDDED_DB"] = "true"
os.environ["KHOJ_ADMIN_EMAIL"] = "admin@khoj.local"
os.environ["KHOJ_ADMIN_PASSWORD"] = "admin123"

print("测试khoj导入...")
from khoj.main import main
print("成功!")
