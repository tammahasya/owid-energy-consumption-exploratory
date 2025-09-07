library(tidyverse)
setwd("/home/zellha/Documents/Dataset/World_Energy_Consumption/")
energy <- read_csv("Fossil_vs_Renew_World.csv")

world <- energy %>% 
  filter(country == "World")

p1 <- ggplot(world, aes(x = year)) +
  geom_line(aes(y = fossil_pct, color = "Fossil Fuels"), size = 1.2) +
  geom_line(aes(y = renew_pct, color = "Renewables"), size = 1.2) +
  scale_color_manual(
    values = c("Fossil Fuels" = "red", "Renewables" = "green")
    ) + 
  theme_minimal()

p1 + labs(
  title = "Global Energy",
  subtitle = "Fossil vs Renewable Energy from 1965 - 2022",
  y = "Share of Total Energy Consumption (%)",
  x = "Year",
  color = "Energy Source",
  caption = "Data from OWID Energy Consumption",
  tags = "P1"
)

top_fossil <- energy %>% 
  filter(year == 2022, country != "World") %>% 
  arrange(desc(fossil_twh)) %>% 
  slice_head(n = 10)

p2 <- ggplot(top_fossil, aes(x = reorder(country, fossil_twh), y = fossil_twh)) +
  geom_col(fill = "red") +
  coord_flip() +
  scale_y_continuous(limits = c(0, 36500)) +
  theme_minimal()
    
p2 + labs(
  title = "Countries by Fossil Energy Usage",
  subtitle = "2022",
  x = "Country",
  y = "Fossil Energy (TWh)",
  caption = "Data from OWID Energy Consumption",
  tags = "P2"
)

top_renew <- energy %>% 
  filter(year == 2022, country != "World") %>% 
  arrange(desc(renewables_twh)) %>% 
  slice_head(n = 10)

p3 <- ggplot(top_renew, aes (x = reorder(country, renewables_twh), y = renewables_twh)) +
  geom_col(fill = "green") +
  coord_flip() +
  scale_y_continuous(limits = c(0, 36500)) +
  theme_minimal()

p3 + labs(
  title = "Countries by Renewables Energy Usage",
  subtitle = "2022",
  x = "Country",
  y = "Renewables Energy (TWh)",
  caption = "Data from OWID Energy Consumption",
  tags = "P3"
)

energy <- energy %>% 
  mutate(renew_fossil_ratio = renewables_twh/fossil_twh)

top_ratio <- energy %>% 
  filter(year == 2022, country != "World") %>% 
  arrange(desc(renew_fossil_ratio)) %>% 
  slice_head(n = 10)

p4 <- ggplot(top_ratio, aes(x = reorder(country, renew_fossil_ratio), y = renew_fossil_ratio)) +
  geom_col(fill = "steelblue") +
  coord_flip() + theme_minimal()

p4 + labs(
  title = "Countries by Renewables-to-Fossil Ratio",
  subtitle = "2022",
  x = "Country",
  y = "Renewables / Fossil (ratio)",
  caption = "Data from OWID Energy Consumption",
  tags = "P4"
)