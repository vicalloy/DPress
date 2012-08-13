@echo off
@call %~dp0..\env\Scripts\activate.bat
@set mg=python.exe %~dp0..\sites\manage.py
@cmd
