@echo off & cls
color 5
title Ps2ExeXobfuscator

start src\ps2exe_installer.cmd
py -m pip install --upgrade colorama requests
cls

type menu.txt
Set /p action="> "
if '%action%'=='1' goto Ps2ExeXobfuscator
if '%action%'=='2' goto Ps2Exe
if '%action%'=='3' goto Obfuscator
if '%action%'=='4' exit

exit
goto end

:Ps2ExeXobfuscator
py src/ps2exeXo_main.py
goto end

:Ps2Exe
py src/ps2exe_m.py
goto end

:Obfuscator
py src/obf_main.py
goto end

:end
pause
exit