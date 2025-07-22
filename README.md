# 🏟️ RCB Stadium Stampede Simulation Dashboard

## 📌 Project Overview

This project simulates a real-world crowd stampede incident at an RCB stadium event to analyze **crowd behavior**, **incident triggers**, and **emergency response readiness** through a **Power BI dashboard**.

The dataset used in this project is **synthetically generated** using Python, but it's modeled closely after **real incident patterns**, backed by **news reports**, **interviews**, and **crowd science case studies** to maintain authenticity.

---

## 🎯 Purpose

Crowd stampedes are unpredictable but often **preventable**. This project aims to:
- Visualize critical risk factors in crowd dynamics
- Track **entry delays**, **security gaps**, and **emotional states**
- Analyze incident patterns and emergency response quality
- Highlight **location-based crowd hotspots**
- Simulate social media reaction trends

---

## 🛠️ Tools & Technologies

| Tool        | Use Case                            |
|-------------|--------------------------------------|
| Python      | Data generation (`pandas`, `faker`, `random`, `datetime`, `numpy`) |
| Power BI    | Dashboard building & data visualization |
| DAX         | KPI calculations & dynamic filters (`DIVIDE`, `CALCULATE`, `COUNTROWS`, `SWITCH`, `SUM`, `AVERAGE`) |

---

## 📊 Dashboards Breakdown

### 1️⃣ Overview Dashboard
- Total incident count, injury severity breakdown
- Timeline of peak incident hours

### 2️⃣ Crowd Behavior & Entry Analysis
- Ticket verification patterns
- Emotional state breakdown
- Gate-wise crowd density & wait time

### 3️⃣ Location Hotspots
- Heatmap of injuries by location
- GPS-based gate-wise panic mapping

### 4️⃣ Emergency Response
- Response time vs. incident severity
- Panic button usage, evacuation strategy types

### 5️⃣ Keyword & Location Trends (Social Media Simulation)
- Trending hashtags during stampede week
- Location-wise tweet count visualization

---

## 📈 Dataset Highlights

- **Records:** 12,567
- **Columns:** 35+
- Key Features:
  - Gate ID, crowd density, ticket status
  - Incident type, injury severity, emotional state
  - Location coordinates (lat, lon)
  - Mode of transportation, behavior flag
  - Crowd control measures, panic button usage
  - Group size, evacuation mode

> 📌 _Note: This is a simulated dataset created for educational and analytical purposes only._

---

## 🔍 Key DAX Measures Used

```DAX
Invalid Ticket % = DIVIDE(CALCULATE(COUNTROWS('RCB_Stampede_Final_Dataset_3'), 'RCB_Stampede_Final_Dataset_3'[ticket_status] = "Invalid"), COUNTROWS('RCB_Stampede_Final_Dataset_3'))
Phase = SWITCH(TRUE(), '4th'[Time] > TIME(18, 45, 0), "Post-Incident", '4th'[Time] > TIME(18, 0, 0), "Incident",'4th'[Time] > TIME(16, 0, 0), "Peak Arrival","Early Arrival")

## ✨ What I Learned
- Simulating real-world events using Python libraries
- Designing BI dashboards for public safety and risk analysis
- Translating complex behavioral data into actionable visuals
- Using DAX to drive dynamic insights

I’d love to hear your feedback or collaborate on related work!
📧 v.jeevesh2004@gmail.com
  
