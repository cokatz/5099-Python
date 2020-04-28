# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:38:37 2020

1. Paste the appropriate code blocks from the Diabetes-Model notebook.
2. Leave the lines for replacing the 0s in insulin commented.
3. Run the file.  Your accuracy should match the Diabetes-Model notebook accuracy - 0.78
    If it doesn't Check your code for errors!
4. You will Run this file twice after you have pasted the appropriate code blocks 
    from the Diabetes-Model notebook and checked your code in step 3
5. Run the file after uncommenting lines  34-35 (Insulin_zero_mean) 
6. Note the accuracy value for run 1.  You will report this value in the assignment on Sakai
7. Comment lines 34-35 and uncomment lines 40-41 (Insulin_nonzero_mean). Rerun the file.
8. Note the accuracy value for run 2.  You will report this value in the assignment on Sakai
9. What is your opinion on why the accuracy changed in the models, 
   which model changed, which way did it change?  in the assignment on Sakai

"""
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression

# Read and load diabetes.csv from my github site
url = 'https://raw.githubusercontent.com/chipshaw/5099-Python/master/Notebooks/assets/diabetes.csv'
diabetesDF = pd.read_csv(url)

# take the mean of the insulin column and replace 0 entries with the mean 

#Run 1: include the zero to generate mean and replace 0's 
#for the first run uncomment the next two lines and run once you have psted all the code blocks below
# Once the code is run look at the value for accuracy and write it down for run 1

#insulin_zero_mean = diabetesDF['Insulin'].mean()
#diabetesDF['Insulin'] = diabetesDF['Insulin'].replace(0, insulin_zero_mean)

#Run 2: do not include the zeroes to generate mean and replace 0's 
# Once the code is run look at the value for accuracy and write it down for run 2

#insulin_nonzero_mean = diabetesDF['Insulin'].replace(0,np.nan).mean(skipna=True)
#diabetesDF['Insulin'] = diabetesDF['Insulin'].replace(0, insulin_nonzero_mean)

# In the Data Prepoaration Data Normailization, and logestic Regression sections of the Diabetes-Model notebook copy the code in the four blocks
# Block one starts with a comment #Total 768 patient records copy the dfTrain through dfCheck lines and paste below



#Block 2 starts with the comment # Separating Label and features ...  Copy the 4 code lines and paste below



#Block 3 Data Normalization Copy and paste all line except the print lines



#Block 4 Logistic Regression copy the top 3 lines and paste below:
