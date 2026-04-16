import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("data.csv")
print(df)

#total spending per customer
print(df.groupby("name")["amount"].sum())#Amit is highest purchaser

#Top customer
print(df.groupby("name")["amount"].sum().idxmax())#Top customer is Priya

#Revenue by city
print(df.groupby("city")["amount"].sum())#Delhi city has highest revenue in cities

#Most popular product
print(df['product'].value_counts())#Most popular product is Laptop

#Average spending per customer
print(df.groupby("name")["amount"].mean())


df.groupby("name")["amount"].sum().plot(kind="bar")
plt.title("Total spending per customer")
plt.show()

df.groupby("city")["amount"].sum().plot(kind="bar")
plt.title("Revenue per city")
plt.show()

sns.countplot(x="product",data=df)
plt.show()