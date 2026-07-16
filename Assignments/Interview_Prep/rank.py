
pythontransactions = [
    {"account_id": "A1001", "txn_date": "2026-06-01", "txn_amount": 1200.50},
    {"account_id": "A1001", "txn_date": "2026-06-15", "txn_amount": 3400.00},
    {"account_id": "A1001", "txn_date": "2026-06-20", "txn_amount": 2100.00},
    {"account_id": "A1002", "txn_date": "2026-06-03", "txn_amount": 800.00},
    {"account_id": "A1002", "txn_date": "2026-06-19", "txn_amount": 6000.00},
    {"account_id": "A1003", "txn_date": "2026-06-05", "txn_amount": 900.00},
    {"account_id": "A1004", "txn_date": "2026-06-10", "txn_amount": 5000.00},
    {"account_id": "A1004", "txn_date": "2026-06-12", "txn_amount": 5000.00},
    {"account_id": "A1004", "txn_date": "2026-06-14", "txn_amount": 3000.00},
]


def second_highest_by_account(transactions):
    amounts_by_account = {}
    for txn in transactions:
        accnt = txn["account_id"]
        amt = txn["txn_amount"]
        amounts_by_account.setdefault(accnt, []).append(amt)

    result = {}
    for k, v in amounts_by_account.items():
        sorted_amounts = sorted(v, reverse=True)
        if len(sorted_amounts) >= 2:
            result[k] = sorted_amounts[1]
        else:
            result[k] = None
    return result
print(second_highest_by_account(pythontransactions))