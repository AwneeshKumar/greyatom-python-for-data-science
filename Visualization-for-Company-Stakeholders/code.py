# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

#Plotting bar plot
plt.bar(loan_status.index,loan_status)


# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.show()



#Changing the x-axis label
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()


#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column
non_graduate = data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate.plot(kind ='density',label='Graduate')

#Plotting density plot for 'Graduate'
non_graduate.plot(kind='density',label='Not Graduate')

#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))


#Plotting scatter plot
plt.scatter(data['ApplicantIncome'],data['LoanAmount'])
plt.title(" Applicant Income")
#Setting the subplot axis title


#Plotting scatter plot
plt.scatter(data['CoapplicantIncome'],data['LoanAmount'])
plt.title(" Coapplicant Income")

#Setting the subplot axis title


#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome']+data['CoapplicantIncome']



#Plotting scatter plot
plt.scatter(data['TotalIncome'],data['LoanAmount'])

plt.title("Total Income")


#Setting the subplot axis title



