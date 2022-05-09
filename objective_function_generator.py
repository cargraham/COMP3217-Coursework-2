import numpy as np
import pandas as pd

#read in the user and task information and convert to NumPy array
user_tasks = pd.read_excel("COMP3217CW2Input.xlsx", sheet_name="User & Task ID", header=0)
user_tasks = np.asarray(user_tasks)

#read in abnormal pricing guidelines
pricing_guidelines = pd.read_excel("TestingResults.xlsx", sheet_name="AbnormalGuidelines", header=0)
pricing_guidelines = np.asarray(pricing_guidelines.iloc[:, 1:-1])

#initialise arrays for neat printing
output_array = []
total_task_array = []
indiv_task_array = []

#set constant variables
USER = "1"
GUIDELINE = "0"

#for each task for the given user
for task in user_tasks:
    task_num = task[0].split("_")
    user = task_num[0].replace("user", "")
    if user == USER:
        user_array = []
        task_array = []
        user_string = ""
        ready_time = task[1]
        deadline = task[2]
        task_num = task_num[1].replace("task", "")
        
        #for each hour in the task
        for x in range(ready_time, deadline + 1):
            user_array.append(str(pricing_guidelines[GUIDELINE, x]) + " x" + task_num + "_" + str(x))
            task_array.append("x" + task_num + "_" + str(x))
            indiv_task_array.append("x" + task_num + "_" + str(x))

        user_string = "+".join(user_array)
        output_array.append(user_string)
        total_task_array.append("+".join(task_array) + "=" + str(task[-1]))

#format the objective function
output_string = "c=" + "+".join(output_array) + ";"

#prints the input for linear programming
print("/* Objective function */")
print("min: c;")
print()
print(output_string)
for task in total_task_array:
    print(task + ";")
for task in indiv_task_array:
    print("0<=" + task + "<=1;")
print()
print("/* Variable bounds */")
