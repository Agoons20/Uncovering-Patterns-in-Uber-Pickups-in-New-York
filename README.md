# Uncovering-Patterns-in-Uber-Pickups-in-New-York: How the Weather, Holidays, and Borough Affect Pickups

#### Situation: 
I read a 2015 article that suggested analytics helped Uber expand its operations in NY and this pushed me to explore the data and see what opportunities there were and how data analytics played a significant role in Uber’s expansion. In 2015, Uber sought to optimize its operations in New York City by understanding factors influencing ride demand. The dataset, covering January–June 2015, includes pickup counts, boroughs, weather conditions (e.g., temperature, precipitation), and holiday indicators, but required preprocessing and analysis to extract actionable insights.

#### Task:  
Identify key drivers of pickup demand and uncover opportunities to boost revenue. This involved loading and cleaning the data, creating time-based features, handling missing values, and conducting exploratory data analysis (EDA) to uncover patterns in boroughs, time, holidays, and weather. The goal was to provide clear, actionable insights for business leaders to optimize driver allocation and pricing strategies.

#### Action:
1.	**Data Import:** Loaded the dataset (Uber Dataset.csv) and verified its structure, ensuring all 29,101 records were correctly ingested.
2.	**Data Preprocessing:** Renamed columns (e.g., spd → wind_speed, hday → holiday) for clarity, converted holiday values (Y/N to Yes/No), and handled 3,043 missing borough values by labeling them as 'Unknown' to preserve data.
3.	**Feature Engineering:** Converted pickup_date to datetime and extracted hour, day_of_week, month, and is_weekend features to analyze temporal patterns.
4.	**Exploratory Data Analysis:**
o	Generated summary statistics to understand data distributions (e.g., average pickups ~490, max 7,883).
o	Created a scatter plot of pickups vs. temperature, revealing a weak positive correlation.
o	Summarized insights, identifying high-demand boroughs (Manhattan, Brooklyn, Queens), peak times (evenings, weekends), holiday effects, and weather impacts.
5.	**Pipeline Development:** Structured the analysis into modular Python scripts (data_import.py, data_preprocessing.py, feature_engineering.py, eda.py) and a Bash script (run_pipeline.sh) for reproducibility, mimicking industry workflows.

#### Result: 
The analysis provided actionable insights for Uber’s NYC operations:
- **Borough:** Manhattan drives most pickups, followed by Brooklyn and Queens.
  
- **Time:** Evening and weekend peaks suggest commuter and leisure demand.
  
- **Holiday:** Slight increase in demand, likely tourism-driven.
  
- **Weather:** Weak effects on pickups, with temperature having slightly positive effect on demands, precipitation/snow having a slightly negative effect on demand.
  
- **EWR:** Zero pickups are surprising for an airport, possibly due to data issues or Uber’s limited airport service in 2015.

**Business Insights:**
- Allocate more drivers to Manhattan, Brooklyn, and Queens, especially during evening hours (5–10 PM) and weekends. Or make driver compensation slightly highly for these three boroughs. 
- Plan for slight demand spikes on holidays for the availability of vehicles, particularly in Manhattan, possibly due to tourism.
- Weather has a minor impact, but prepare for reduced demand during heavy rain or snow. Also, give drivers more incentives during low precipitation periods to maintain service to the population.
- 
These insights enable Uber to allocate drivers efficiently, adjust pricing dynamically, and plan for seasonal and weather-related demand fluctuations, improving operational efficiency and customer satisfaction.

