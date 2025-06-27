import pandas as pd

# Load the raw dataset
df = pd.read_csv("outputs/uber_raw.csv")

# Rename columns for clarity
df = df.rename(columns={
    'hday': 'holiday',
    'spd': 'wind_speed',
    'temp': 'temp',
    'dewp': 'dew_point',
    'vsb': 'Visibility',
    'slp': 'Sea.level.pressure',
    'pcp01': '1h_Precipitation',
    'pcp06': '6h_Precipitation',
    'pcp24': '24h_Precipitation',
    'pickup_dt': 'pickup_date',
    'sd': 'snow_depth'
})

# Update holiday values for readability
df['holiday'] = df['holiday'].replace('Y', 'Yes')
df['holiday'] = df['holiday'].replace('N', 'No')

# Handle missing values in borough (correcting the original error)
df['borough'] = df['borough'].fillna('Unknown')  # Replace NaN with 'Unknown'

# Display borough value counts
print("Borough value counts after handling missing values:")
print(df['borough'].value_counts(dropna=False))

# Save the preprocessed dataset
df.to_csv("outputs/uber_preprocessed.csv", index=False)
print("\nPreprocessed dataset saved as 'outputs/uber_preprocessed.csv'")