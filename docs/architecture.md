# 🧠 AI-Based Autonomous Navigation System Architecture

## 📌 Overview
This project simulates an autonomous agent navigating in a grid environment using the A* path planning algorithm.

---

## 🔁 Workflow

1. Environment Creation  
2. Obstacle Placement  
3. Path Planning (A*)  
4. Navigation Execution  
5. Visualization  

---

## 🧩 Modules

### 1. Environment Module (`environment.py`)
- Generates grid
- Adds obstacles randomly

### 2. Path Planner (`path_planner.py`)
- Implements A* algorithm
- Finds shortest path

### 3. Navigator (`navigator.py`)
- Simulates agent movement

### 4. Visualization (`visualization.py`)
- Displays path and obstacles
- Saves output image

---

## 🔄 Data Flow

Grid → Obstacles → A* Path → Navigation → Visualization

---

## 📊 Architecture Diagram

Environment
   ↓
Obstacle Detection
   ↓
Path Planning (A*)
   ↓
Navigation
   ↓
Visualization

---

## 🎯 Features
- Autonomous navigation
- Obstacle avoidance
- Path optimization

---

## 🚀 Future Improvements
- YOLO object detection
- Real-time simulation
- Self-driving car model