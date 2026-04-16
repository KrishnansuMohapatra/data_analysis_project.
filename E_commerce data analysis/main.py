import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("data.csv")
print(df)
#Creating new column called revenue"""
df["revenue"]=df["quantity"]*df["price"]
print(df)
#total revenue
total_revenue=df["revenue"].sum()
print("Total revenue is",total_revenue)

#Revenue by product
revenue_by_product=df.groupby("product")["revenue"].sum()
print("Revenue by ",revenue_by_product)

#Revenue by customer
revenue_by_customer=df.groupby("customer")["revenue"].sum()
print("Revenue by customer",revenue_by_customer)
print("Top customer is",revenue_by_customer.idxmax())

#Monthly trend
revenue_by_month=df.groupby("month")["revenue"].sum()
print("Revenue by month",revenue_by_month)
print(f"The  {revenue_by_month.idxmax()} month has highest revenue")

#most ordered products
most_ordered_product=df.groupby("product")["quantity"].sum()
print("Most ordered products are",most_ordered_product)
print("Most ordered products is",most_ordered_product.idxmax())

#Visulization
revenue_by_product.plot(kind="bar")
plt.title("Revenue by product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

revenue_by_month.plot(kind="line")
plt.title("Revenue by month")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

sns.countplot(x="product",data=df)
plt.show()