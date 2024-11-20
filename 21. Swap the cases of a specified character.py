import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Swap the case of the 'City' column
df['City'] = df['City'].str.swapcase()

print(df)
