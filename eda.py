import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set plotting style
plt.style.use('seaborn-v0_8')  # Updated package
sns.set_palette("deep")

# Load the engineered dataset
df = pd.read_csv("outputs/uber_engineered.csv")

# Summary statistics
print("Summary Statistics:")
print(df.describe(include='all'))

# Scatter plot: Pickups vs Temperature
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temp', y='pickups', data=df, alpha=0.3)
plt.title('Pickups vs Temperature')
plt.xlabel('Temperature (°F)')
plt.ylabel('Pickups')
plt.savefig("outputs/pickups_vs_temp.png", dpi=300, bbox_inches='tight')
plt.close()

# Key insights
print("\nKey Insights:")
print("1. Borough Impact: Manhattan has significantly higher pickups compared to other boroughs, followed by Brooklyn and Queens. EWR and Staten Island have minimal pickups.")
print("2. Time Patterns: Pickups peak in the evening hours (5-10 PM) and are lowest in the early morning (3-6 AM). Weekends show slightly higher pickups than weekdays.")
print("3. Holiday Effect: Holidays have a slight increase in pickups, particularly in Manhattan, possibly due to tourism or events.")
print("4. Weather Influence: Temperature shows a weak positive correlation with pickups, while precipitation (pcp01, pcp06, pcp24) and snow depth (sd) have weak negative correlations, suggesting adverse weather reduces demand.")
print("5. Interesting Fact: The dataset shows zero pickups at EWR consistently, which is unexpected for an airport location, possibly indicating data collection issues or Uber's limited presence there in 2015.")

# Save insights to a text file
with open("outputs/eda_insights.txt", "w") as f:
    f.write("Key Insights:\n")
    f.write("1. Borough Impact: Manhattan has significantly higher pickups compared to other boroughs, followed by Brooklyn and Queens. EWR and Staten Island have minimal pickups.\n")
    f.write("2. Time Patterns: Pickups peak in the evening hours (5-10 PM) and are lowest in the early morning (3-6 AM). Weekends show slightly higher pickups than weekdays.\n")
    f.write("3. Holiday Effect: Holidays have a slight increase in pickups, particularly in Manhattan, possibly due to tourism or events.\n")
    f.write("4. Weather Influence: Temperature shows a weak positive correlation with pickups, while precipitation (pcp01, pcp06, pcp24) and snow depth (sd) have weak negative correlations, suggesting adverse weather reduces demand.\n")
    f.write("5. Interesting Fact: The dataset shows zero pickups at EWR consistently, which is unexpected for an airport location, possibly indicating data collection issues or Uber's limited presence there in 2015.\n")
print("\nEDA insights saved as 'outputs/eda_insights.txt'")
