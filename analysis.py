import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')

# Read the CSV file
df = pd.read_csv("D:\coding work\IBM financial data analysis\Finance_data.csv")

# Drop unwanted columns
df.drop(['Mutual_Funds', 'Equity_Market',
       'Debentures', 'Government_Bonds', 'Fixed_Deposits', 'PPF', 'Gold'], axis=1, inplace=True)

# Convert the 'gender' column to categorical explicitly
df['gender'] = pd.Categorical(df['gender'])

# First we will see Gender of our respondents
sns.countplot(data=df, x='gender', linewidth=3, palette="Set2", edgecolor='black')
#plt.show()

# Now we will see Age of our respondents
sns.countplot(df['age'],palette="Set3",linewidth=2,edgecolor='black')
#plt.show()

# Now lets see these same factors of INVESTMENT_AVENUE and STOCK_MARKET with gender

plt.figure(figsize=(18,6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['gender'],hue=df['Investment_Avenues'],palette='summer',linewidth=3,edgecolor='white')
plt.title('INVESTMENT AVENUE')
plt.subplot(1, 2, 2)
sns.countplot(x=df['gender'],hue=df['Stock_Marktet'],palette='hot',linewidth=3,edgecolor='white')
plt.title('STOCK MARKET')
plt.show()


# # Mostly females dont invest or go to stocks 

# # Factors affecting Investing 
# sns.countplot(x=df['Factor'],palette='coolwarm',linewidth=2,edgecolor='black')

# # Returns is the most influential Factor considered while investing which is followed by risk 

# # Lets see which Age groups take the highest risk 
# sns.countplot(x=df['gender'],hue=df['Factor'],palette='Oranges',linewidth=2,edgecolor='black')
# plt.title('Gender')
# plt.show()

# plt.figure(figsize=(16,6))
# sns.pointplot(x="Purpose",y='age',data=df,linestyles="--",capsize=.3,color='Red')
# plt.show()

# # Now lets see these same factors of Duration and Invest_monitor with gender

# plt.figure(figsize=(18,6))
# plt.subplot(1, 2, 1)
# sns.countplot(hue=df['gender'],x=df['Duration'],palette='viridis',linewidth=2,edgecolor='black')
# plt.title('DURATION')
# plt.subplot(1, 2, 2)
# sns.countplot(hue=df['gender'],x=df['Invest_Monitor'],palette='seismic',linewidth=2,edgecolor='black')
# plt.title('INVESTMENT MONITORING')
# plt.show()