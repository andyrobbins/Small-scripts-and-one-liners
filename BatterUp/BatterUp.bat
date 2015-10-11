@echo off
REM Batch port of selected modules from PowerUp by harmj0y
REM Author: @_wald0
SETLOCAL ENABLEDELAYEDEXPANSION

REM ======================================
REM = Find unquoted service binary paths =
REM ======================================
echo(
echo Finding unquoted service binary paths...
echo(

for /f "tokens=2* delims=:" %%i in ('sc query ^|findstr "SERVICE_NAME"') do (
    set str=%%i
	set str=!str:~1!
    sc qc "!str!" | findstr "BINARY_PATH_NAME" | findstr /iv "c:\windows\\" | findstr /iv """
)

REM ========================================================================
REM =                 Check permissions on services                        =
REM =           Technique stolen from PowerUp by harmj0y                   =
REM = https://github.com/HarmJ0y/PowerUp/blob/master/PowerUp.ps1#L104-L141 =
REM ========================================================================
echo(
echo Finding service binaries your user has write access to...
echo(

for /f "tokens=2* delims=:" %%i in ('sc query ^|findstr "SERVICE_NAME"') do (
    set str=%%i
	set str=!str:~1!
	for /f "tokens=4" %%e in ('sc qc "!str!" ^| findstr "ERROR_CONTROL"') do (
	    set errCtrl=%%e
		sc config "!str!" error= !errCtrl! > nul && (
		        echo Vulnerable service found: !str!
		)
    )
)

REM =================================================
REM = Check for write access to directories in PATH =
REM =================================================
echo(
echo Finding write access in PATH directories...
echo(

REM http://stackoverflow.com/a/14879373
for %%A in ("%path:;=";"%") do (
    set filename=%%~A\dll-write-check.txt
	copy /y nul "!filename!" > nul 2>&1 && (
	    del "!filename!"
	    echo Writable path directory found: %%A
	)
)
