@echo off

REM - A simple Script to resolve "Unhandled Exception" on the ECC App
REM - Author: Ibor Offor | Designation: Technical Manager | Year: 2024

cd C:\Users\ECC\AppData\Local\NCC_Case_System\NCC_Case_System.exe_Url_1claezvvoktxaehwgbbu0fpstsfoljsd\1.0.0.0
del user.config
cd "C:\Program Files (x86)\AroSoft Technology\ECCAPPSetup\NCC_Case_System"
start NCC_Case_System.exe