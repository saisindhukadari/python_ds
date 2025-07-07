import pandas as pd

# Define the data dictionary
data = {
    'name': ["a", "b", "c", "d", "e"],
    'age': [24, 35, 26, 45, 29],
    'dept': ["IT", "CSE", "IOT", "IT", "CSE"],
    'salary': [15000, 250000, 4500, 80000, 89000],
    'joindate': ['2022-06-01', '2021-08-05', '2023-06-01', '2021-08-06', '2023-08-06']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'joindate' column to datetime
df['joindate'] = pd.to_datetime(df['joindate'])

# Add new column for joining year
df['joiningyear'] = df['joindate'].dt.year

# Add a column to categorize seniority
df['seniority'] = df['age'].apply(lambda x: 'senior' if x > 30 else 'junior')

# Print final DataFrame
print(df)

# Save DataFrame to CSV
df.to_csv("employee.csv", index=False)