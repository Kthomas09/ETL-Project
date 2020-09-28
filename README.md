# George Washington University Data Analytics Boot Camp 2020 Fall Cohort

Assignment: ETL Project
Group members: Temitayo "David" Olanbiwonnu, Jennifer S, Kent L. Thomas, Cynthia Zhang

Topic: United States COVID-19 Demographic Data in Relation to States Data

Summary:
This is a project to extract, transform, and load state COVID-19 data into a postgress database. This is an extension to our previous project entitled "GWU Project 1" where we extracted, cleaned, and visualize critical COVID-19 data analyzing geographic and demographic information. In this project we set out to make the data more current, responsive, and develop a more sustainable way of storing the state COVID-19 data. 

## Extraction:

Kent L. Thomas:

We extracted data from two seperate data sources originiating from the Postman COVID-19 API Resource Center. The first API calls The Covid-Tracking Project API which gives a variety of state COVID-19 testing data in real time beginning from the start of the covid-19 pandemic. The second data source was derived from the COVID-19 Finnhub API. Next called in the API JSON, and convert the JSON into a csv and export the csv's into the Resource folder (us_covid_tracking_data.csv & covid_testing_data.csv). 

## Transformation: 

Jennifer S & Cynthia Zhang:

When cleaning and transforming the data, we imported the csv files into the ETL Queries jupyternotebook. Next, using functions getTypes, describeData and analyzeNaNs's, we get the dataset dtypes, statistics, NaN counts and length, before and after cleaning. This was done to verify changes in datasets were made and accurate. In order to match the Covid Tracking data set we had to drop all the data except the most recent day to match the FinnHub API data set. We next removed the columns that were not a necessity. In order to merge the two data sets, we had to change the names of the state names in the FinnHub data to the state abbreviation. Finally we merged the two datasets, changed the names of various columns to help load the data, and exported the merged csv file (combinedCovidData.csv). 

## Load

Temitayo "David" Olanbiwonnu: 

The final step to the project is to created the postgres database using pgAdmin4. We created a SQL file to create the state_covid_19_db and loaded the data by importing the csv.

Resources:
1) Postman Covid-19 API's: 
https://covid-19-apis.postman.com/
2) Covid-Tracking Project:
https://documenter.getpostman.com/view/8854915/SzS8rjHv?version=latest#72fa1e45-55fb-467b-909a-4040791bf9a7
3) Finnhub COVID-19
https://documenter.getpostman.com/view/10724784/SzYW3LFa?version=latest
