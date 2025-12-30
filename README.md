# 📚 AIN-3003 Project 1: Kubernetes Bookstore API

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

Hi there! This is my first project for the AIN-3003 course. I built a containerized Python Flask API that talks to a MongoDB database, all running on a local Kubernetes cluster.

## 🚀 What's Inside?
* **Full CRUD API:** You can Add, List, Update, and Delete books using Python and Flask.
* **Stateful Database:** I used a **Kubernetes StatefulSet** for MongoDB to make sure my data stays safe even if the database pod restarts.
* **Dockerized:** The whole app is containerized using Docker.
* **Service Discovery:** The Flask app finds the MongoDB instance automatically using Kubernetes Services.

## 🛠️ Tech Stack
* **Backend:** Python (Flask)
* **Database:** MongoDB
* **Containers:** Docker
* **Orchestration:** Kubernetes

## 📖 How to Run it
If you want to run this system on your machine, follow these steps:

1. **Build the Docker Image:**
   `docker build -t python-app:v1 .`

2. **Deploy MongoDB (StatefulSet):**
   `kubectl apply -f mongodb.yaml`

3. **Deploy the Flask App:**
   `kubectl apply -f flask_app.yaml`

4. **Test it:**
   Go to `http://localhost:5000/books` in your browser to see the book list!

## 📸 Screenshots
You can find all the terminal logs, service lists, and browser tests in my project report (PDF).
