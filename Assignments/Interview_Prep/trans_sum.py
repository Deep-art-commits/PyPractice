'''
Question 1 (Python, foundations — no pandas):
You have a list of transactions, each one a dictionary:

Write a function that takes this list and returns a dictionary mapping each account_id to its total transaction amount
— the plain-Python equivalent of the GROUP BY account_id, SUM(txn_amount) you already know cold in SQL.
'''

pythontransactions = [
    {"account_id": "A1001", "txn_date": "2026-06-01", "txn_amount": 1500.50},
    {"account_id": "A1001", "txn_date": "2026-06-15", "txn_amount": 3400.00},
    {"account_id": "A1002", "txn_date": "2026-06-03", "txn_amount": 800.00},
    {"account_id": "A1001", "txn_date": "2026-06-20", "txn_amount": 2100.00},
    {"account_id": "A1002", "txn_date": "2026-06-19", "txn_amount": 6000.00},
]
def accounts_over_threshold(transactions, threshold):
    totals = {}
    count={}
    for txn in transactions:
        accnt = txn["account_id"]
        amt = txn["txn_amount"]
        totals[accnt] = totals.get(accnt, 0) + amt
        count[accnt]  = count.get(accnt,0)+1

    result_sum = []
    result_count=[]
    for k, v in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        if v > threshold:
            result_sum.append((k, v))
    for  k,v in sorted(count.items(),key=lambda x: x[1], reverse=True):
        if v>2:
            result_count.append((k,v))
    return result_sum,result_count