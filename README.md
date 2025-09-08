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

To illustrate different perspectives, this project combines **R**, **Tableau**, and **Spreadsheets** for visualization:  

- **Global Trend (Spreadsheet):** Shows how fossil fuels dominate historically, but renewables are starting to grow.  
- **Geospatial View (Tableau):** Highlights country-level distribution of renewable adoption in 2022.  
- **Efficiency Ratio (R):** Identifies countries with the best renewables-to-fossil ratio, showing relative efficiency in adopting clean energy.  

<p align="center">
  <img src="spreadsheet/Energy_Consumption_Over_Years.png" alt="Energy Trend" width="450"/>
  <img src="tableau/Tableau Example 2022.png" alt="Geo Tableau" width="450"/>
  <img src="r/Best_Efficiency.png" alt="Best Efficiency Ratio" width="450"/>
</p>

---

## License
This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
