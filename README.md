# Weather Data Storage System

## 📖 Assignment Details
- **Course Code**: ENCS205 
- **Semester**: 3rd  
- **Theme**: Foundation of Data Structures  
- **Language Used**: Python  

This project implements a **Weather Data Storage System** using **2D arrays** and **Abstract Data Types (ADTs)**.  
It allows efficient storage, retrieval, and analysis of weather data (temperature by city and year).  

---

## 🎯 Objectives
- Understand Abstract Data Types (ADT) and 2D arrays in Python.  
- Implement a real-world data storage system.  
- Compare **row-major vs column-major access**.  
- Handle **sparse data** using sentinel values.  
- Analyze **time and space complexity** of operations.  

---

## ⚙️ Features
1. **WeatherRecord ADT**  
   - Attributes: `date`, `city`, `temperature`  
   - Methods: Insert, Delete, Retrieve  

2. **WeatherDataStorage Class**  
   - Stores data in a 2D array (years × cities).  
   - Supports:  
     - `insert()` → Add weather data  
     - `delete()` → Remove weather data  
     - `retrieve()` → Get temperature for city & year  
     - `rowMajorAccess()` → Access row-wise  
     - `columnMajorAccess()` → Access column-wise  
     - `handleSparseData()` → Replace missing values with sentinel (-999)  
     - `analyzeComplexity()` → Shows time & space complexity  

---

## 🖥️ Example Output
Row Major: [15.5, None, None, None, 28.2, None, None, None, 22.1]
Column Major: [15.5, None, None, None, 28.2, None, None, None, 22.1]
Retrieve (Delhi, 2023): 15.5
Sparse Representation: {(2023, 'Delhi'): 15.5, (2024, 'Mumbai'): 28.2, (2025, 'Kolkata'): 22.1}

--- Complexity Analysis ---
Insert: O(1)
Delete: O(1)
Retrieve: O(1)
Row/Column Access: O(nm)
Space Complexity: O(nm)

