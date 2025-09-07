SELECT
  year,
  SUM(fossil_fuel_consumption) AS fossil_twh,
  SUM(renewables_consumption) AS renewables_twh,
  SUM(fossil_fuel_consumption + renewables_consumption) AS total_twh,
  ROUND(SUM(fossil_fuel_consumption) / SUM(fossil_fuel_consumption + renewables_consumption) * 100, 2) AS fossil_pct,
  ROUND(SUM(renewables_consumption) / SUM(fossil_fuel_consumption + renewables_consumption) * 100, 2) AS renew_pct
FROM
  `daring-glider-469510-k9.world_energy_consumption.energy_consumption`
WHERE
  country = 'World'
  AND year IS NOT NULL
  AND fossil_fuel_consumption IS NOT NULL
  AND renewables_consumption IS NOT NULL
GROUP BY
  year
ORDER BY
  year;
