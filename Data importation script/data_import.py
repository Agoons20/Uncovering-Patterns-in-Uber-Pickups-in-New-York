import pandas as pd
import os

# B sure to import numpy if you'd like to do further data exploration 
# Create outputs directory if it doesn't exist
if not os.path.exists('outputs'):
    os.makedirs('outputs')

# Load the dataset
df = pd.read_csv("Uber Dataset.csv")

# Display the first three rows to inspect the data structure
print("First three rows of the dataset:")
print(df.head(3))

# Save the raw dataset for reference
df.to_csv("outputs/uber_raw.csv", index=False)
print("\nRaw dataset saved as 'outputs/uber_raw.csv'")
