# **Lambda Architecture for Climate Data Processing & Visualization**  


## 🚀 **Description**  

This project implements a **Lambda Architecture** to enable **climate data processing and visualization** from the **OpenWeatherMap API**. The architecture combines **real-time data processing** with **historical data storage**, allowing advanced analysis and interactive dashboards.  

The goal is to ensure **automated, scalable data management** while providing comprehensive insights into weather trends and patterns.  

With this system, users can visualize **real-time and historical weather insights** via **dynamic dashboards**, gaining an operational, real-time perspective of climate conditions.  

---

## 📊 **Dataset Description**  

### **Source**  
Data collected from [OpenWeatherMap API](https://openweathermap.org/api)  

### **Domain**  
Real-time climate conditions.  

### **Data Types**  
-  Temperature  
-  Precipitation  
-  Wind speed  
-  Humidity  
-  Atmospheric pressure  
-  Other climate indicators  

---

## 🎯 **Project Objectives**  

### **1️⃣ Batch Layer**  
-  Set up robust data processing pipelines for analyzing historical data.  
-  Store precomputed views for efficient and rapid querying.  



### **2️⃣ Speed Layer (Real-Time Layer)**  
-  Process real-time data streams with low latency for dynamic insights.  
-  Enable live updates for up-to-the-minute climate information.  



### **3️⃣ Serving Layer**  
- Provide combined insights from batch and real-time layers.  
- Ensure quick and efficient data querying for visualization purposes.  

---

## ⚙️ **Quick Start Guide**  

Before starting, make sure you have the following prerequisites:



###  **Prerequisites**  

To get started, ensure the following software and environment are installed:  

- 🐳 **Docker Desktop**  
- 🐍 **Python**  
- 💻 **At least 16GB of RAM**  
- 🖥️ **Git**  
- 📊 **Tableau**  

---

### **How To Run**  

Follow the steps below to set up the project:

1️⃣ **Clone the Repository**  

```bash
git clone https://github.com/whoamiisroot/lambda-architecture-openweather-api
```
2️⃣ **Launch the Infrastructure with Docker Compose**

```bash
cd lambda-architecture-openweather-api
docker-compose up --build
```
## **Architecture Overview**

The system relies on **Lambda Architecture**, structured into three interconnected layers. Below is a visual representation of the architecture:
![Ajouter des lignes dans le corps du texte (2)](https://github.com/user-attachments/assets/abaae215-f3fd-4fcd-b01d-3ea653d93075)
