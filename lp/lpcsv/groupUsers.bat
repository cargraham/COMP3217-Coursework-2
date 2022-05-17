@echo off
setlocal enableDelayedExpansion 

REM sort all csv files into subdirectories according to their guidelines
for %%i in (*.csv) do (
	set filename=%%i
	set foldername=!filename:~0,-11!
	echo !foldername!
	if not exist !foldername! mkdir !foldername!
	move !filename! !foldername!
)

REM for each subdirectory combine all guidelines into one csv file and place in parent directory
for /R /D %%i in (*) do (
	cd %%i
	copy *.csv %%~ni.csv
	move %%~ni.csv ..
	cd ..
)
PAUSE