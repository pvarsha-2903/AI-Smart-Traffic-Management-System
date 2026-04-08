AI Smart Traffic Management System (PRAVAH)

## Overview
This project is an AI-powered Smart Traffic Management System designed to reduce traffic congestion using adaptive signal timing.

Originally developed for Smart India Hackathon, this version is expanded for India-wide deployment.

## Problem
Traffic congestion causes:

- Time loss
- Fuel waste
- Pollution
- Emergency delays

Current traffic signals use fixed timing, which is inefficient.

## Solution
This system uses:

- AI
- Traffic simulation
- Vehicle detection
- Adaptive signal control

to dynamically adjust traffic lights based on traffic density.

## Features
- Fairness-based traffic control (prevents starvation of lanes)
- Dynamic signal switching using vehicle count and wait time
- Real-time traffic simulation
- Visual traffic representation using symbols/emojis
- AI-based vehicle detection (planned)

## ⚙️ How It Works
1. Each lane has vehicle count and wait time
2. A fairness formula is applied:
   Priority = Vehicles + (Wait Time × 0.7)
3. The lane with the highest priority gets the green signal
4. Other lanes wait, increasing their priority over time
5. This ensures no lane is ignored (prevents starvation)

## 📊 Simulation Output

(Screenshot will be added soon)

## Tech Stack
- Python
- GitHub
- OpenCV (future)
- Flask (future)

## 📄 Smart India Hackathon Submission

This project was originally proposed during Smart India Hackathon 2025.

[View SIH Presentation](./PRAVAH-SIH-Presentation.pdf)
  

## Project Status
Phase 1: Documentation and Simulation

## Author
## Team – Civaura (Smart India Hackathon 2025)

This project was originally developed as part of Smart India Hackathon 2025 by Team Civaura.

## Maintained and Extended by
Varsha Penumudi and Aarya Bhandari

