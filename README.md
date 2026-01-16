# Transaction Analyzer

## About

**Transaction Analyzer** is a simple Python project that analyzes customer transaction data. The script processes a list of transaction records, extracts key details such as transaction ID, amount, and timestamp, and then generates useful insights.

This project was built to practice core Python concepts like string manipulation, loops, sorting, and basic data analysis.

---

## Features

* Extracts transaction ID, amount, and timestamp from raw transaction strings
* Calculates and displays the highest and lowest transaction amounts
* Sorts transactions based on timestamp for chronological analysis
* Uses basic Python logic without external libraries

---

## Technologies Used

* Python 3.x
* `datetime` module for parsing and sorting timestamps

---

## How to Run

1. Clone or download the repository
2. Make sure Python 3.x is installed
3. Open a terminal or command prompt
4. Navigate to the project folder and run:

```bash
python transaction_analyzer.py
```

---

## Sample Input

```python
transactions = [
    "1, 200, 2024-11-17 09:45:23",
    "2, -50, 2024-11-17 09:47:00",
    "3, 100, 2024-11-18 10:00:00",
    "4, 150, 2024-11-17 11:00:00",
    "5, -20, 2024-11-19 09:00:00"
]
```

---

## Sample Output

```text
Transaction Summary:
===================
Highest Transaction: 200.0
Lowest Transaction: -50.0

Transactions (Sorted by Timestamp):
===================================
2024-11-17 09:45:23
2024-11-17 09:47:00
2024-11-17 11:00:00
2024-11-18 10:00:00
2024-11-19 09:00:00
```

---

## How It Works

* The script reads a list of transaction strings
* Each transaction is split into transaction ID, amount, and timestamp
* The program identifies the highest and lowest transaction values
* Transactions are sorted using timestamps to display them in order

---

## Notes

This project is intended for learning and practice. You can extend it by:

* Adding transaction summaries per customer
* Handling invalid or malformed data
* Exporting results to a file
