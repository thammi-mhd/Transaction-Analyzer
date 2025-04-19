# Transaction-Analyzer

## About

Welcome to the **Transaction Analyzer** project! This simple Python script is designed to analyze customer transaction data. It takes a list of transactions, extracts key details like transaction ID, amount, and timestamp, and then provides some useful insights:

- The highest and lowest transaction amounts.
- A sorted list of transactions based on the timestamp, so you can easily see when they occurred.

This is a great project to practice basic Python concepts like string manipulation, loops, and sorting.

## 🧰 Features
- Breaks down each transaction into its components: Transaction ID, Amount, and Timestamp.
- Calculates and displays the highest and lowest transaction amounts.
- Sorts transactions by timestamp so you can see the order of events.
- Uses simple Python techniques to process data and display the results.

## ⚙️ Technologies Used
- **Python 3.x** – The main programming language used for this project.
- **`datetime` module** – Used for handling and formatting timestamps.

## 🚀 How to Run
1. Clone or download the repo to your local machine.
2. Make sure you have Python 3.x installed (you can download it from [python.org](https://www.python.org/)).
3. Open a terminal or command prompt, navigate to the project folder, and run:
   ```bash
   python transaction_analyzer.py
📊 Sample Input
Here’s an example of how the transaction data looks:
```python
transactions = [
    "1, 200, 2024-11-17 09:45:23",
    "2, -50, 2024-11-17 09:47:00",
    "3, 100, 2024-11-18 10:00:00",
    "4, 150, 2024-11-17 11:00:00",
    "5, -20, 2024-11-19 09:00:00"
]
```

🖥️ Sample Output
Once you run the script, you’ll see something like this:
```python
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


🤔 How It Works
The script takes a list of transaction strings, each containing a transaction ID, amount, and timestamp.

It splits these strings into their individual components.

The program then calculates the highest and lowest transaction amounts.

Finally, the transactions are sorted by their timestamps to display them in the correct order.

Feel free to tweak the code, experiment with different inputs, or add new features to the script as you continue learning Python. Enjoy building!

markdown
Copy
Edit

### What’s different in this version:
```
1. **Friendly tone**: The language is more conversational and welcoming.
2. **Shorter sections**: Each section is concise and to the point.
3. **Clear explanations**: The description and usage are more approachable, explaining technical terms in simple language.
4. **Inviting for modifications**: The last part encourages users to make changes and learn from the project.
```
