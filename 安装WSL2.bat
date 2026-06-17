@echo off
chcp 65001 >nul
echo ========================================
echo   WSL2 安装脚本 (需要管理员权限)
echo ========================================
echo.

echo [1/3] 启用 WSL 功能...
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
echo.

echo [2/3] 启用 虚拟机平台...
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
echo.

echo [3/3] 安装 WSL2 (包含Ubuntu)...
wsl --install --no-distribution
echo.

echo ========================================
echo   完成！请重启电脑，然后启动 Docker Desktop
echo ========================================
pause
