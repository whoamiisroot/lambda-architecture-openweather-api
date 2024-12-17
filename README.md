🚀 Description
This project implements a Lambda Architecture to enable climate data processing and visualization from the OpenWeatherMap API. The architecture combines real-time data processing with historical data storage to allow advanced analysis and interactive dashboards. The goal is to ensure automated and scalable data management while providing comprehensive insights into weather trends and patterns.

With this system, users can visualize real-time and historical weather insights via dynamic dashboards, gaining a comprehensive operational view of climate conditions.

📊 Dataset Description
Source: Data collected from the OpenWeatherMap API.
Domain: Historical and real-time climate conditions.
Data Types: Temperature, precipitation, wind speed, atmospheric pressure, humidity, and other climate indicators.
Significance:
Visualize and analyze real-time climate data.
Explore historical climate trends for planning and prediction purposes.
Integrate insights into actionable decision-making processes.

🎯 Project Objectives
Batch Layer:

Set up robust data processing pipelines for analyzing historical data.
Store precomputed views for efficient and rapid querying.
Speed Layer (Real-Time Layer):

Process real-time data streams with low latency for dynamic insights.
Enable live data updates for an up-to-the-minute climate view.
Serving Layer:

Provide combined results from batch and real-time layers through an efficient user query interface.
Ensure quick access to insights through optimized data delivery.


⚙️ Quick Start Guide
Prerequisites
Before you get started, ensure you have the following installed:

Docker desktop 
Python
At least 32GB of RAM (recommended)
Git
Tableau


📥 Installation Steps
Clone the repository:
bash
Copier le code
git clone https://github.com/whoamiisroot/lambda-architecture-openweather-api
Launch infrastructure with Docker Compose:
bash
Copier le code
docker-compose up -d
