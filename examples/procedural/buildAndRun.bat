@echo off
c:\Workspace\NES\nesfab_1_8\nesfab.exe .\procedural.cfg
if %ERRORLEVEL% EQU 0 (
    c:\Workspace\NES\Mesen\Mesen.exe procedural.nes
)
