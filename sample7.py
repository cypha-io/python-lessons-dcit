# Write a program that does the following:

# Asks the user how many items they are buying

# Uses a for loop to collect the name of each item

# Stores the items in a list

# After the loop, prints:

count_items = int(input("How many items are you buying?: "))

items_db = []

for i in range(count_items):
    item_name = input(f"Enter the name of item {i + 1}: ")
    items_db.append(item_name)

print("\nItems you are buying:")
for item in items_db:
    print(f"{item}")
