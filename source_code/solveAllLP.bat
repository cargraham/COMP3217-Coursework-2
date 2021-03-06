@echo off
setlocal enableDelayedExpansion 

REM move necessary files into the subdirectory 'lp'
move lp_solve.exe lp
move AxesTitles.bas lp
move GraphMakerMacro.bas lp
move csv2xlsm.vbs lp

REM change directory into subdirectory 'lp'
cd lp

REM make directory 'lpcsv' if it doesn't already exist
if not exist lpcsv mkdir lpcsv

REM move necessary files into the subdirectory 'lpcsv'
move AxesTitles.bas lpcsv
move GraphMakerMacro.bas lpcsv
move csv2xlsm.vbs lpcsv

REM solve each linear programming file using the command line LP_Solve application
for %%i in (*.lp) do (
	lp_solve %%i > lpcsv\%%~ni.csv
)

REM change directory into subdirectory 'lpcsv'
cd lpcsv

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

REM convert all csv files in directory to xlsm
for %%i in (*.csv) do (
	csv2xlsm.vbs "%%~fi"
	del %%i
)

REM change directory up to root directory twice
cd ..\..