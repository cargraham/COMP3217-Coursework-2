#version of python to use
PYTHON = python

.PHONY = help setup run

.DEFAULT_GOAL = run

help:
	@echo ---------------HELP-----------------
	@echo To run the project type 'make'
	@echo ------------------------------------
	
run:
	mkdir lp
	@echo The following results were used to compare the available algorithms' accuracies so one could be chosen to implement from scratch. Please see report for details.
	${PYTHON} sklearn_algorithm_comparison.py
	@echo The following results are the accuracies obtained from the manual implementation of the Gaussian Naive Bayes classifier
	${PYTHON} training_guideline_model.py
	@echo The linear programming files are being generated and saved under a subdirectory named 'lp'
	${PYTHON} objective_function_generator.py
	@echo The linear programming files are being solved using the command line version of LP_Solve
	solveAllLP.bat
	
setup: 
	pip install -r requirements.txt
	
