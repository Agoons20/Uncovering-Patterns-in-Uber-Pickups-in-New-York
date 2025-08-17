import pandas as pd

# Load the preprocessed dataset
df = pd.read_csv("outputs/uber_preprocessed.csv")

# Convert 'pickup_date' to 'datetime' 
df['pickup_date'] = pd.to_datetime(df['pickup_date'])

# Extract time-based features from 'pickup_date' variable 
df['hour'] = df['pickup_date'].dt.hour
df['day_of_week'] = df['pickup_date'].dt.dayofweek
df['month'] = df['pickup_date'].dt.month
df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)

# Display data types to verify changes were successfully
print("Data types after feature engineering:")
print(df.info())

# Save the dataset with new features
df.to_csv("outputs/uber_engineered.csv", index=False)
print("\nDataset with engineered features saved as 'outputs/uber_engineered.csv'")
