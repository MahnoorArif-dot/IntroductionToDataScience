def find_unique_users(transactions):
    
    unique_users = set()  
    for transaction in transactions:
        unique_users.add(transaction[1])  
    return len(unique_users)

def highest_transaction(transactions):
    highest=transactions[0]
    for transcation in transactions:
        if transcation[2]>highest[2]:
            highest=transcation
    return highest
        

def separate_ids(transactions):
   
    transaction_ids = []
    user_ids = []
    
    for transaction in transactions:
        if len(transaction) != 4:
            raise ValueError(f"Inconsistent tuple size: {transaction}")
        transaction_ids.append(transaction[0])  
        user_ids.append(transaction[1])  
    
    return transaction_ids, user_ids

transactions_data = [
    (1, 'user1', 450.00, '2024-10-15 11:45:23'),
    (2, 'user2', 560.30, '2024-10-15 11:11:11'),
    (3, 'user3', 600.40, '2024-10-12 09:50:12'),
    (4, 'user2', 400.50, '2024-10-12 14:09:10'),
    (5, 'user1', 130.00, '2024-10-11 08:0507:30')
]
unique_user_count = find_unique_users(transactions_data)
print("Total Unique Users:", unique_user_count)
highest_tx = highest_transaction(transactions_data)
print("Transaction with the Highest Amount:", highest_tx)
transaction_ids, user_ids = separate_ids(transactions_data)
print("Transaction IDs:", transaction_ids)
print("User IDs:", user_ids)
