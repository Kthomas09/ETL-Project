DROP TABLE IF EXISTS state_covid_19 ;

CREATE TABLE state_covid_19 (
  todays_date DATE,
  positive FLOAT,
  negative FLOAT,
  death_increase VARCHAR(30),
  state  VARCHAR(30),
  total_cases INT,
  death INT,
	updated VARCHAR(30),
	state_abrv VARCHAR(30)
); 

COPY state_covid_19(todays_date, positive, negative, death_increase, state, total_cases, death, updated, state_abrv)
FROM '/Users/kent.thomas/Repository/ETL-Project/Resources/combinedCovidData.csv'
DELIMITER ','
CSV HEADER;
	
SELECT *
FROM state_covid_19;

-- Temitayo "David" Olanbiwonnu