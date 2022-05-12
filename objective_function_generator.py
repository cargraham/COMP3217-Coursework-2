import numpy as np
import pandas as pd

#read in the user and task information and convert to NumPy array
user_tasks = pd.read_excel("COMP3217CW2Input.xlsx", sheet_name="User & Task ID", header=0)
user_tasks = np.asarray(user_tasks)

#read in abnormal pricing guidelines
pricing_guidelines = pd.read_excel("TestingResults.xlsx", sheet_name="AbnormalGuidelines", header=0)
pricing_guidelines = np.asarray(pricing_guidelines)

#creates a NumPy array of the guideline row numbers
pricing_guidelines_nums = pricing_guidelines[:, 0]

#the guidelines without row numbers 
pricing_guidelines = pricing_guidelines[:, 1:-1]

#for each user from 1-5
for user_num in range(1,6):

    #initialise a counter to retrieve guidelines from NumPy array
    guideline_counter = 0
    
    for guideline_num in pricing_guidelines_nums:
        guideline_num = int(guideline_num)

        #creates a file for the current guideline and user
        file = "lp/guideline-" + str(guideline_num) + "-user-"+ str(user_num) + ".lp"
        file = open(file, 'w')

        #initialise arrays to use for neat printing
        output_array = []
        total_task_array = []
        indiv_task_array = []
        
        for task in user_tasks:
            task_num = task[0].split("_")
            user = task_num[0].replace("user", "")
            if int(user) == user_num:
                user_array = []
                task_array = []
                user_string = ""
                ready_time = task[1]
                deadline = task[2]
                task_num = task_num[1].replace("task", "")
                guideline = pricing_guidelines[guideline_counter, :]
                
                #for each hour in the task
                for x in range(ready_time, deadline + 1):
                    user_array.append(str(guideline[x]) + " x" + task_num + "_" + str(x))
                    task_array.append("x" + task_num + "_" + str(x))
                    indiv_task_array.append("x" + task_num + "_" + str(x))

                user_string = "+".join(user_array)
                output_array.append(user_string)
                total_task_array.append("+".join(task_array) + "=" + str(task[-1]))

        #format the objective function
        output_string = "c=" + "+".join(output_array) + ";"

        #wirtes the input for linear programming to the file
        file.write("/* Objective function */\n")
        file.write("min: c;\n\n")
        file.write(output_string + "\n")
        for task in total_task_array:
            file.write(task + ";\n")
        for task in indiv_task_array:
            file.write("0<=" + task + "<=1;\n")
        file.write("\n")
        file.write("/* Variable bounds */")
        file.close()
        
        guideline_counter += 1
