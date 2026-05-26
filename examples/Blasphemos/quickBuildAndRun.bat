@echo off
cls

echo Starting Quick Build Pipeline (Dev Version)...

python scripts/mapfab_to_json.py
if %errorlevel% neq 0 exit /b %errorlevel%

python scripts/split_maps.py
if %errorlevel% neq 0 exit /b %errorlevel%

python scripts/update_version.py
if %errorlevel% neq 0 exit /b %errorlevel%

echo Building Dev version...
python scripts/set_build_flag.py dev
if %errorlevel% neq 0 exit /b %errorlevel%

c:\Workspace\NES\nesfab_1_8\nesfab.exe .\BlasNESmous.cfg
if %errorlevel% neq 0 exit /b %errorlevel%

copy /Y BlasNESmous.nes BlasNESmous_dev.nes
copy /Y BlasNESmous.mlb BlasNESmous_dev.mlb

echo Launching Mesen...
start "" c:\Workspace\NES\Mesen\Mesen.exe BlasNESmous_dev.nes
