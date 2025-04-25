# IMMO-ELIZA - Data Exploration - Κωνσταντινούπολις
## Description 
ImmoEliza, a real estate company aiming to become the market leader in Belgium, seeks to enhance its strategic decisions using data-driven insights. To support this mission, the company envisions a machine learning model capable of predicting property prices across the Belgian market.

As a preliminary step, ImmoEliza requested an in-depth exploratory data analysis (EDA) of a scraped real estate dataset. This analysis aims to uncover patterns, correlations, and insights that could guide the development of a future predictive model.

This project includes:
- Data cleaning and preprocessing
- Descriptive statistics and visualization
- Geographical and regional price comparisons
- Feature correlation and relevance for price prediction

By understanding the key drivers of property prices, ImmoEliza will be better positioned to identify the most valuable listings and make smarter investment decisions.

## Dependecies
Install these dependencies: 
```
!pip install seaborn
!pip install folium
!pip install pgeocode
```
"Run All" on the Notebook

## Usage : 
### 1. Data Cleaning
#### Remove columns
```
columns=["Unnamed: 0", "url"]
columns=['monthlyCost', 'hasBalcony', 'accessibleDisabledPeople', 
         'roomCount', 'diningRoomSurface', 'streetFacadeWidth',
         'gardenOrientation', 'kitchenSurface', 'floorCount', 
         'hasDiningRoom', 'hasDressingRoom', 'hasAttic']
```
#### Remove duplicate(s)
```
df.drop_duplicates(subset=["id"], keep="first")
```
#### Handle missing values and convert types
- Binary encoding: We converted boolean columns (e.g., hasBasement, hasLift, etc.) into 0/1 values, handling missing data accordingly.
- Missing value imputation: We filled in missing values using medians, modes, or logical assumptions (e.g., hasThermicPanels = 0 when not specified).
- Type conversion: We standardized data types (int, float, str) based on the nature of each column.

### 2. Data Analysis
- Correlation Heatmap
- Prices Histogram
- Price per square meter
- Boxplots of prices per differents features
- Map prices

### 3. Data Interpretation
- Looking at prices histogram we decided to separate houses and apartments that are less and more expensive than 1,000,000
- We also decided to visualize houses and appartments seperatly
- On map visualizations, we decided to remove outliers (more than 90%)

### 4. Bonus
#### Tableau public :
[See Tableau HERE]( https://public.tableau.com/views/Houses_Belgium/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)


### Contributors
- [Alex](https://github.com/Fillinger66)
- [Natthawadee](https://github.com/Winwi21)
- [Quentin](https://github.com/Zohrr-26)
- [Robin](https://github.com/Rhodham96)

