# E-commerce Order Analysis Project

## 📌 Objective

Analyze e-commerce order data to understand customer behavior, product performance, and revenue trends.

---

## 🛠 Tools & Technologies

* Python
* Pandas
* Matplotlib
* Seaborn

---

## 📊 Dataset Description

The dataset contains the following columns:

* **order_id** → Unique order identifier
* **customer** → Customer name
* **product** → Product purchased
* **quantity** → Number of items purchased
* **price** → Price per item
* **month** → Month of purchase

A new column **revenue** is created using:

```
revenue = quantity × price
```

---

## 📈 Analysis Performed

### 1. Total Revenue

* Calculated total revenue generated from all orders

### 2. Revenue by Product

* Identified which product generates the most revenue

### 3. Revenue by Customer

* Analyzed spending behavior of customers

### 4. Top Customer

* Identified the highest spending customer

### 5. Monthly Revenue Trend

* Analyzed how revenue changes over time

### 6. Most Ordered Product

* Identified product with highest total quantity sold

---

## 📊 Visualizations

* Bar chart → Revenue by product
* Line chart → Monthly revenue trend
* Count plot → Product frequency

---

## 🔍 Key Insights

* **Laptop generates the highest revenue**
* **Customer A is the top customer**
* Revenue varies across months with a clear trend
* **Phone/Laptop are the most frequently ordered products**

---

## 📁 Project Structure

```
ecommerce-analysis/
│
├── data.csv
├── analysis.py
├── README.md
```

---

## 🚀 Conclusion

This project demonstrates:

* Data transformation and feature engineering
* Aggregation using pandas (`groupby`)
* Business insight extraction
* Data visualization using matplotlib and seaborn

---

## 🎯 Outcome

This project showcases practical skills required for **Data Analyst roles**, including data manipulation, analysis, and visualization of business data.
