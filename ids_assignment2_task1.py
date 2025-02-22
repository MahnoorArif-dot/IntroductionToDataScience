def filter(data):
    
    names_list = []  
    for user in data:
        if user[2] > 30 and user[3] in ('USA', 'Canada'):
            names_list.append(user[1])  
    return names_list

def process_user_data(data):
    
   
    sorted_data = sorted(data, key=lambda x: x[2], reverse=True)
    top10 = sorted_data[:10] 
    names = [user[1] for user in data]

    duplicates=set()
    for name in names:
        if names.count(name)>1:
            duplicates.add(name)
            
    
    return top10, duplicates

user_data = [
    (1, 'Mahnoor', 33, 'USA'),
    (2, 'Hajra', 28, 'Canada'),
    (3, 'Sidra', 48, 'USA'),
    (4, 'Rabia', 50, 'UK'),
    (5, 'Musqan', 29, 'USA'),
    (6, 'Armish', 34, 'Canada'),
    (7, 'Zarish', 38, 'Germany'),
    (8, 'Kainat', 22, 'Canada'),
    (9, 'Alishbha', 42, 'USA'),
    (10, 'Mahnoor', 55, 'Canada'),
    (11, 'Mehak', 60, 'USA')
]

filtered_names = filter(user_data)
print("Filtered Names:", filtered_names)

top_10_oldest, duplicate_names = process_user_data(user_data)
print()
print("Top 10 Oldest Users:", top_10_oldest)
print()
print("Duplicate Names:", duplicate_names)
