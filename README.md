# Weather Data Storage System

## 📖 Assignment Details
- **Course Code**: ENCS205 
- **Semester**: 3rd  
- **Theme**: Foundation of Data Structures  
- **Language Used**: Python  

This project implements a **Weather Data Storage System** using **2D arrays** and **Abstract Data Types (ADTs)**.  
It allows efficient storage, retrieval, and analysis of weather data (temperature by city and year).  

## 📖 Problem
We need to build a **Weather Data Storage System** using Python.  
The system should store temperature values for cities and years in a **2D array**,  
allow insertion, retrieval, and comparison of **row major vs column major** access.  
It should also handle **sparse data** using a sentinel value.  

---

## ✨ Features
1. **WeatherRecord ADT** → stores date, city, and temperature.  
2. **WeatherDataStorage** → class with methods:  
   - `insert()` → insert a record  
   - `retrieve()` → get temperature by city & year  
   - `row_major()` → row-wise access  
   - `column_major()` → column-wise access  
   - `handle_sparse()` → replace missing values with sentinel (-999)  
   - `analyze_complexity()` → shows time and space complexity  

---

## 🖥️ Example Output
Row Major: [15.5, None, None, None, 28.2, None, None, None, 22.1]
Column Major: [15.5, None, None, None, 28.2, None, None, None, 22.1]
Retrieve (Delhi, 2023): 15.5
Sparse Data: [[15.5, -999, -999], [-999, 28.2, -999], [-999, -999, 22.1]]

--- Complexity Analysis ---
Insert: O(1)
Retrieve: O(1)
Row/Column Access: O(nm)
Space: O(nm)
****
📚 References

GeeksforGeeks – Sparse Matrix Representations

W3Schools – Python Arrays

