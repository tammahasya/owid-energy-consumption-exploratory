SELECT
  year,
  country,
  iso_code,
  SUM(fossil_fuel_consumption) AS fossil_twh,
  SUM(renewables_consumption) AS renewables_twh,
  SUM(fossil_fuel_consumption + renewables_consumption) AS total_twh,
  ROUND(SUM(fossil_fuel_consumption) / SUM(fossil_fuel_consumption + renewables_consumption) * 100, 2) AS fossil_pct,
  ROUND(SUM(renewables_consumption) / SUM(fossil_fuel_consumption + renewables_consumption) * 100, 2) AS renew_pct
FROM
  `daring-glider-469510-k9.world_energy_consumption.energy_consumption`
WHERE
  year >= 1965
  AND fossil_fuel_consumption IS NOT NULL
  AND renewables_consumption IS NOT NULL
  AND (iso_code IS NOT NULL OR iso_code = 'world')
GROUP BY
  year, iso_code, country
ORDER BY
  year, country;
