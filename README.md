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

## 📊 Sample Visualizations

### Plot 1 — Energy Consumption per Capita Trend (Spreadsheet)
<img src="spreadsheet/Energy per Capita.png" alt="Energy per Capita Trend" width="600"/>

This trend shows how global energy consumption per capita has changed over time. The steady increase reflects growing industrialization, urbanization, and higher living standards worldwide. However, the growth is uneven, with certain regions contributing disproportionately to the rise.  

---

### Plot 2 — Geospatial Renewables View (Tableau)
<img src="tableau/Tableau Example 2022.png" alt="Geo Tableau" width="600"/>

This Tableau visualization highlights the distribution of renewable energy adoption across countries in 2022. While China leads in absolute terms, other regions such as Europe show stronger proportional adoption. This provides insight into where renewable energy investment and policy efforts are most advanced.  

---

### Plot 3 — Renewables-to-Fossil Efficiency Ratio (R)
<img src="r/Best_Efficiency.png" alt="Best Efficiency Ratio" width="600"/>

This plot shows the top 10 countries ranked by the ratio of renewables to fossil energy usage in 2022. Smaller countries often appear near the top because their reliance on renewables is proportionally higher. This metric gives a fairer comparison of which nations are truly transitioning toward cleaner energy systems.  

---

## License
This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
