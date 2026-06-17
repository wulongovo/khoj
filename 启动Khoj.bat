@echo off
chcp 65001 >nul
set PYTHONPATH=
set VIRTUAL_ENV=

echo ========================================
echo   Khoj - AI第二大脑
echo   访问: http://localhost:42110
echo   管理员: admin@khoj.local / khoj2026
echo   Ctrl+C 停止
echo ========================================

cd /d E:\Khoj
"C:\Users\ZhuanZ1\.conda\envs\pytorch\python.exe" E:\Khoj\start.py
pause
