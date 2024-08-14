import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt


# Use forward slashes in the file path
s = "C:/Users/NISHANTH/Downloads/Lab Session Data.xlsx"

# Load the correct sheet name
data = pd.read_excel(s, sheet_name='IRCTC Stock Price')

# Extract relevant columns for matrix A
price = data[['Price']]
price_matrix=price.to_numpy()
print(price_matrix)
sum=0
c=0
print(price_matrix)
for i in price_matrix:
    for j in i:
        sum=sum+j
        c=c+1

print("The sum is",sum)
total_mean=sum/c
print("The mean or average is",total_mean)
variance=0
for i in price_matrix:
    for j in i:
        variance=variance+((j-total_mean)**2)/c
print("THe variance is",variance)


print('_')

wednesday_data=data[data['Day']=='Wed']
wed_prices=wednesday_data['Price']
sum_p=0
cnt=0
print(wed_prices)
for p in wed_prices:

    print(p)
    sum_p += p
    cnt=cnt+1

wed_mean=sum_p/cnt
print("The mean or average is",wed_mean)
difference1=np.sqrt((wed_mean-total_mean)**2) #to get mod
print("On comparision the difference in total price and price on only wednesdays is ",difference1)
print('_')
April_data=data[data['Month']=='Apr']
apr_prices=April_data['Price']
sum_p=0
cnt=0
print(apr_prices)
for p in apr_prices:

    print(p)
    sum_p += p
    cnt=cnt+1

apr_mean=sum_p/cnt
print("The mean or average is",apr_mean)
difference2=np.sqrt((apr_mean-total_mean)**2)
print("On comparision the difference in total price and price on only wednesdays is ",difference1)


# Extract the Chg% data from column I
chg_data = data['Chg%']

# Calculate the probability of making a loss
loss_probability = len([x for x in chg_data if x < 0]) / len(chg_data)

print("Probability of making a loss:", loss_probability)


# Extract the Chg% data for Wednesdays
wednesday_chg_data = wednesday_data['Chg%']

# Calculate the probability of making a profit on Wednesdays
profit_probability_wednesday = len([x for x in wednesday_chg_data if x > 0]) / len(wednesday_chg_data)

print("Probability of making a profit on Wednesday:", profit_probability_wednesday)


# Calculate the total probability of making a profit
profit_probability = len([x for x in chg_data if x > 0]) / len(chg_data)

# Calculate the conditional probability of making a profit given it is Wednesday
conditional_profit_probability_wednesday = profit_probability_wednesday / (len(wednesday_data) / len(data))

print("Conditional probability of making a profit given that today is Wednesday:", conditional_profit_probability_wednesday)



# Create a scatter plot of Chg% against the day of the week
days_of_week = data['Day']
chg_percent = data['Chg%']

plt.scatter(days_of_week, chg_percent)
plt.xlabel('Day of the Week')
plt.ylabel('Chg%')
plt.title('Chg% vs. Day of the Week')
plt.show()