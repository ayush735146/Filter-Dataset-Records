import pandas as pd

# Sample dataset
data = {
    "Name": ["Ayush", "Rahul", "Priya", "Neha", "Aman", "Riya"],
    "Age": [19, 21, 18, 22, 20, 23],
    "Marks": [85, 72, 91, 68, 79, 88],
    "City": ["Mathura", "Agra", "Mathura", "Delhi", "Agra", "Delhi"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Example 1: Filter students with marks greater than 80
filtered_marks = df[df["Marks"] > 80]
print("\nExample 1 - Marks > 80:")
print(filtered_marks)

# Example 2: Filter students from Mathura
filtered_city = df[df["City"] == "Mathura"]
print("\nExample 2 - City is Mathura:")
print(filtered_city)

# Example 3: Multiple conditions
filtered_multiple = df[(df["Marks"] >= 80) & (df["Age"] < 22)]
print("\nExample 3 - Marks >= 80 AND Age < 22:")
print(filtered_multiple)

# Number of records
print("\nRecord counts:")
print("Marks > 80:", len(filtered_marks))
print("City = Mathura:", len(filtered_city))
print("Marks >= 80 and Age < 22:", len(filtered_multiple))
