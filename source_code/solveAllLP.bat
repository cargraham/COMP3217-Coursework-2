@echo off
setlocal enableDelayedExpansion 

move lp_solve.exe lp
move AxesTitles.bas lp
move GraphMakerMacro.bas lp
move csv2xlsm.vbs lp

cd lp

if not exist lpcsv mkdir lpcsv
move AxesTitles.bas lpcsv
move GraphMakerMacro.bas lpcsv
move csv2xlsm.vbs lpcsv

REM solve each linear programming file using the command line LP_Solve application
for %%i in (*.lp) do (
	lp_solve %%i > lpcsv\%%~ni.csv
)

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

cd ..\..