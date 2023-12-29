## Production Fixed Horizon Planning with Python 🏭
*Implement the Wagner-Whitin algorithm to minimize the total costs of production given a set of constraints*

<p align="center">
  <img align="center" src="https://miro.medium.com/max/786/1*0gFQPmIuKcGLL7j9G3geQw.png">
</p>

### Objective
Use python to design an optimal production plan to meet customer demand and minimize the total production costs.

### Article
In this [Article](https://towardsdatascience.com/production-fixed-horizon-planning-with-python-8dd38b468e86), we will implement optimal production planning using 
the Wagner-Whitin method with python.

### 📘 Your complete guide for Supply Chain Analytics
60+ case studies with source code, dummy data and mathematical concepts here 👉 [Analytics Cheat Sheet](https://bit.ly/supply-chain-cheat)

### Youtube Video
Click on the image below to access a full tutorial video to understand the concept behind this solution
<div align="center">
  <a href="https://www.youtube.com/watch?v=130AKb2DejM"><img src="https://i.ytimg.com/vi/130AKb2DejM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFTyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB14U22DUisLrmIqh5gCIlzVNGAog" alt="Explainer Video Link"></a>
</div>

### Scenario
You are a production planning manager in a small factory producing radio equipment that serves local and international markets.

Customers send Purchase Orders (PO) to your commercial team with quantities and expected delivery dates.

Your role is to schedule production to deliver on time with a minimum total cost of production that includes

- Setup Costs: fixed costs you have each time you set up a production line
- Production Costs: variable costs per unit produced
- Holding Costs: cost of storage per unit per time
- In our example, the customer ordered products for the next 12 months

<p align="center">
  <img align="center" src="https://miro.medium.com/proxy/1*64ql0685ZVlvW7GJ47VAoA.png">
</p>

#### Wagner-Whitin Algorithm
This problem can be seen as a generalization of the economic order quantity model that takes into account that demand for the product varies over time.

Wagner and Whitin developed an algorithm for finding the optimal solution by dynamic programming.

The idea is to understand each month if adding the current month's demand quantity to past months' orders can be more economic than setting up a new cycle of production.

<p align="center">
  <img width=60% align="center" src="https://miro.medium.com/max/828/1*UBJpFl8kb7J3s8SytsWPcw.png">
</p>

## Code
This repository code you will find all the code used to explain the concepts presented in the article.

## About me 🤓
Senior Supply Chain Engineer with an international experience working on Logistics and Transportation operations. \
Have a look at my portfolio: [Data Science for Supply Chain Portfolio](https://samirsaci.com) \
Data Science for Warehousing📦, Transportation 🚚 and Demand Forecasting 📈 

