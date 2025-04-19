from datetime import date

transactions = [
    "1, 200, 2024-11-17 09:45:23",
    "2, -50, 2024-11-17 09:47:00",
    "3, 100, 2024-11-18 10:00:00",
    "4, 150, 2024-11-17 11:00:00",
    "5, -20, 2024-11-19 09:00:00"
]

def transaction_details(transactions):
    tra_1 = {}
    temp_var = []
    all_amount = []
    all_timestamp = []
    
    for i in range(0, len(transactions)):
        tra_1[i+1] = transactions[i]
    
    for key, value in tra_1.items():
        temp_var = value.split(",")
        amount = float(temp_var[1].strip())
        timestamp = temp_var[2].strip()

        all_amount.append(amount)
        all_timestamp.append(timestamp)

    max_amt = max(all_amount)
    min_amt = min(all_amount)

    print("Transaction Summary Analysis:")
    print("="*30)
    print(f"Highest Transaction Amount: {max_amt}")
    print(f"Lowest Transaction Amount: {min_amt}")
    
    print("\nTransactions Sorted by Timestamp:")
    print("="*30)
    for timestamp in sorted(all_timestamp):
        print(timestamp)

transaction_details(transactions)
