## Production Fixed Horizon Planning with Python 🏭
*Implement the Wagner-Whitin algorithm to minimise the total costs of production given a set of constraints*

<p align="center">
  <a href="https://www.samirsaci.com/production-fixed-horizon-planning-with-python/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://miro.medium.com/max/786/1*0gFQPmIuKcGLL7j9G3geQw.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

### Objective
Use Python to design an optimal production plan that meets customer demand and minimises total production costs.

### Article
In this [Article](https://www.samirsaci.com/production-fixed-horizon-planning-with-python/), we will implement optimal production planning using the Wagner-Whitin method with Python.

### 📘 Your complete guide for Supply Chain Analytics
60+ case studies with source code, dummy data and mathematical concepts here 👉 [Analytics Cheat Sheet](https://bit.ly/supply-chain-cheat)

### Youtube Video
Click on the image below to access a full tutorial video to understand the concept behind this solution
<div align="center">
  <a href="https://www.youtube.com/watch?v=130AKb2DejM"><img src="https://i.ytimg.com/vi/130AKb2DejM/hqdefault.jpg?sqp=-oaymwEcCNACELwBSFTyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB14U22DUisLrmIqh5gCIlzVNGAog" alt="Explainer Video Link"></a>
</div>

### Scenario
You are a production planning manager at a small factory producing radio equipment for local and international markets.

Customers submit Purchase Orders (POs) to your commercial team, including quantities and expected delivery dates.

Your role is to schedule production to deliver on time with a minimum total cost of production that includes

- Setup Costs: fixed costs you have each time you set up a production line
- Production Costs: variable costs per unit produced
- Holding Costs: cost of storage per unit per time
- In our example, the customer ordered products for the next 12 months

<p align="center">
  <img align="center" src="https://miro.medium.com/proxy/1*64ql0685ZVlvW7GJ47VAoA.png">
</p>

#### Wagner-Whitin Algorithm
This problem can be seen as a generalisation of the economic order quantity model that takes into account that demand for the product varies over time.

Wagner and Whitin developed an algorithm for finding the optimal solution by dynamic programming.

The idea is to understand each month if adding the current month's demand quantity to past months' orders can be more economic than setting up a new cycle of production.

<p align="center">
  <img width=60% align="center" src="https://miro.medium.com/max/828/1*UBJpFl8kb7J3s8SytsWPcw.png">
</p>

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

## About me 🤓
Senior Supply Chain and Data Science consultant with international experience working on Logistics and Transportation operations.\
For **consulting or advising** on analytics and sustainable supply chain transformation, feel free to contact me via [Logigreen Consulting](https://www.logi-green.com/)\
Please have a look at my personal blog: [Personal Website](https://samirsaci.com)
