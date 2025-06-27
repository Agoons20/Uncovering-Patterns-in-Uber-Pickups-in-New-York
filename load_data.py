import pandas as pd
import os

# Print working directory
print("Working Directory:", os.getcwd())

# Load dataset
df = pd.read_csv("Uber Dataset.csv")

# Display basic info
print("\nFirst few rows:")
print(df.head(3))
print("\nLast few rows:")
print(df.tail(3))
print("\nDimensions:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nDataset Info:")
print(df.info())

# Save raw data info
with open("output/raw_data_info.txt", "w") as f:
    f.write("First few rows:\n")
    f.write(str(df.head(3)))
    f.write("\n\nLast few rows:\n")
    f.write(str(df.tail(3)))
    f.write(f"\n\nDimensions: {df.shape}")
    f.write("\n\nColumn names: " + ", ".join(df.columns.tolist()))

# Save raw dataset (optional)
df.to_csv("output/raw_uber_data.csv", index=False)
print("\nRaw dataset saved as 'output/raw_uber_data.csv'")