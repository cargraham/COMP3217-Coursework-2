for %%i in (*.lp) do (
	lp_solve %%i > lpcsv\%%~ni.csv
)