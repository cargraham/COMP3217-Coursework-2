for /R /D %%i in (*) do (
	cd %%i
	copy *.csv %%~ni.csv
	move %%~ni.csv ..
	cd ..
)
PAUSE