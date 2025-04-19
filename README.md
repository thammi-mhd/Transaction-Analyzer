# Transaction-Analyzer


This Python project processes and analyzes a list of transactions. It extracts transaction IDs, amounts, and timestamps, identifies the highest and lowest transaction amounts, and sorts transactions by timestamp.

#🔧 Features
- Extracts and separates transaction ID, amount, and timestamp.
- Identifies the maximum and minimum transaction amounts.
- Sorts transactions by time.
- Splits timestamp into date and time format.

#🧠 Technologies Used
- Python 3.x
- datetime module

#💻 How to Run
1. Clone or download the repo.
2. Run the Python script:
   ```bash
   python transaction_analyzer.py

#SAMPLE INPUT:-
transactions = [
    "1, 200, 2024-11-17 09:45:23",
    "2, -50, 2024-11-17 09:47:00",
    "3, 100, 2024-11-18 10:00:00",
    "4, 150, 2024-11-17 11:00:00",
    "5, -20, 2024-11-19 09:00:00"
]

#OUTPUT EXAMPLE:-
max amount in the transaction is: 200 
and the minimum amount that is in transaction is: -50
['2024-11-17 09:45:23', '2024-11-17 09:47:00', '2024-11-17 11:00:00', '2024-11-18 10:00:00', '2024-11-19 09:00:00']
