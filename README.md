# OWID Energy Consumption Exploratory Analysis
"Multi-tool exploratory analysis of fossil vs renewable energy (1965-2022) using OWID dataset"
Exploratory analysis of global energy consumption using the [OWID dataset](https://www.kaggle.com/datasets/pralabhpoudel/world-energy-consumption), combining **SQL**, **Tableau**, **R**, and **Spreadsheets** to explore fossil vs renewable energy trends.

---

## Project Structure
```
data/
├─ World Energy Consumption.csv # Raw dataset
├─ Fossil_vs_Renew.csv # Processed for Tableau
└─ Fossil_vs_Renew_World.csv # Processed for R (includes World)

r/
├─ World_Energy_Consumption_Exploration_Analysis.R
├─ Energy_Share.png
├─ Top_Fossil.png
├─ Top_Renewables.png
└─ Best_Efficiency.png

spreadsheet/
├─ World_Energy_Consumption_Processed.csv
├─ Energy Consumption Over Years.png
├─ Energy Consumption per Capita 2020.png
├─ Energy per Capita.png
└─ Primary Energy Consumption 2020.png

sql/
├─ Energy_Consumption_Percentage.sql
└─ Energy_Consumption_Percentage_World.sql

tableau/
└─ Tableau Example 2022.png
```

---

## Insights
- **Global trend (1965–2022):** Fossil fuels still dominate, but renewables are rising.
- **Top fossil consumers:** China, USA, India continue to lead fossil energy use.
- **Top renewable consumers:** China leads in absolute renewable energy, but ratio analysis shows smaller countries may be more efficient in renewables adoption.
- **Renewables-to-Fossil ratio:** Provides a fairer view of which countries are truly transitioning to clean energy.

---

##  Tools Used
- **SQL** → Data aggregation and percentage share calculations  
- **Spreadsheets** → Quick trend exploration & per-capita comparisons  
- **R (tidyverse)** → Advanced visualizations and ratio analysis  
- **Tableau Public** → Interactive geospatial & temporal dashboards  

---

## Sample Visualizations
![Global Energy Share](r/Energy_Share.png)
*Fossil vs Renewable energy share worldwide (1965–2022)*

![Top Fossil Users](r/Top_Fossil.png)
*Top 10 countries by fossil energy usage in 2022*

![Top Renewables Users](r/Top_Renewables.png)
*Top 10 countries by renewables energy usage in 2022*

![Efficiency Ratio](r/Best_Efficiency.png)
*Top 10 countries by Renewables-to-Fossil ratio in 2022*

---

## License
This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
