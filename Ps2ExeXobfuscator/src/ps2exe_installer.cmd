@echo off
setlocal

powershell -Command "if (Get-Module -ListAvailable -Name PS2EXE) { exit 0 } else { exit 1 }"

if %errorlevel% neq 0 (
    echo PS2EXE module is not installed. Installing...
    powershell -Command "Install-Module -Name PS2EXE -Force -Scope CurrentUser"
    if %errorlevel% equ 0 (
        echo PS2EXE module installed successfully.
    ) else (
        echo Failed to install PS2EXE module.
    )
) else (
    echo PS2EXE module is already installed.
)

endlocal
exit