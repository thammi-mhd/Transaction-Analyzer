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
  all_date = []
  all_time = []
  all_amount = []
  all_tid = []
  all_timestamp = []
  
  timestamp_real  = []
  dt_verification = "2024-11-17"
  for i in range(0,len(transactions)):
    tra_1[i+1] = transactions[i]
  for key, value in tra_1.items():
      temp_var = value.split(",")
      tid = temp_var[0].strip()  
      amount = temp_var[1].strip()  
      timestamp = temp_var[2].strip() 

      all_tid.append(tid)
      all_amount.append(amount)
      all_timestamp.append(timestamp)
  max_amt = max(all_amount)
  min_amt = min(all_amount)
  print("max amount in the transaction is: ",max_amt,"\n and the minimum amount that is in transaxtion is: ",min_amt)
  desc_sort_timesatmp = sorted(all_timestamp)
  print(desc_sort_timesatmp)
  for i in all_timestamp:
     timestamp_real.append(i.split(" "))
  
        
        
transaction_details(transactions)