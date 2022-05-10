for %%i in (*.csv) do (
	csv2xlsm.vbs "%%~fi"
)
PAUSE