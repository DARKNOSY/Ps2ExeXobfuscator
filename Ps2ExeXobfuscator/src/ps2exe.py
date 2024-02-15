import os, json

with open("src/config.json") as f:
    config = json.load(f)

ps_script = config["ps_script"]
exe_name = config["exe_name"]
icon = config["icon"]
icon_path = config["icon_path"]
title = config["title"]
description = config["description"]
product = config["product"]
company = config["company"]
copyright_ = config["copyright"]
trademark = config["trademark"]
version = config["version"]

if not os.path.exists(ps_script):
    print("File not found. Please check the file path and try again.")
    exit()

obfuscated_ps_script = ps_script.replace(".ps1", "_obfuscated.ps1")
output_exe = ps_script.replace(".ps1", ".exe")

os.system(f'powershell -command "(Get-Content \'{ps_script}\') | Out-File \'{obfuscated_ps_script}\' -Encoding UTF8"')

if icon == "True":
    os.system(f'powershell -command "Invoke-ps2exe .\\{ps_script} .\\{exe_name}.exe -iconFile \'{icon_path}\' -title \'{title}\' -description \'{description}\' -company \'{company}\' -product \'{product}\' -copyright \'{copyright_}\' -trademark \'{trademark}\' -version \'{version}\'"')
else:
    os.system(f'powershell -command "Invoke-ps2exe .\\{ps_script} .\\{exe_name}.exe -title \'{title}\' -description \'{description}\' -company \'{company}\' -product \'{product}\' -copyright \'{copyright_}\' -trademark \'{trademark}\' -version \'{version}\'"')

os.remove(obfuscated_ps_script)

print("Transformation completed!")