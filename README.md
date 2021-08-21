# Household Electricity Consumption per capita
## Introduction
From statistics, countries with big population like china and US rank as the largest household electricity consumer.
This result is obvious and not enough to create a deep intuition. I wanted to go see the data in the individual level.
What if global electricity consumption amount is divided by population?
The result figures are shown on the world map and on the bar chart respectively.
Unlike ranks of the most electricity consuming country, top countries per capita household electricity consumption are set in this order; Iceland, Norway, Bahrain, Kuwait and Canada.


## Analysis procedure
1. Collecting Data.
  * World Map: List of countries, locations and shapes of countries. [Source](https://thematicmapping.org/downloads/world_borders.php)
  * Population: List of countries and their population. Webscraped the data from Wikipedia. [Source](https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations))
  * Household Electricity Consumption: List of countries, Electricity Consumption [Source](http://data.un.org/Data.aspx?d=EDATA&f=cmID%3aEL%3btrID%3a1231)

2. Cleaning Data.
  * There is some missing data in population and electricity figures. 
  * Some of them were added from different sources. 
  * Other countries with lacking values were dropped because most of them are tiny islands where people do not consume much electricity and their population is under 10,000. Removing those values does not impact the consequences.

3. Merging and Modifying Data.
  * Three data can relate to each other by countries. Some names of countries are displayed in different ways in each dataset. With intention to standardize names, a couple of conversion rules are applied: Removing apostrophe and abbreviation. Other cases that those rules are not applied are manually handled.
  * New column is added: Household Electricity Consumption per country / Population.
 
4. Plotting Data.
  * Sort by newly appended column. 
  * Create a bar chart with top 20 countries.
  * Create choropleth map with new column.
--- 
![top20](https://user-images.githubusercontent.com/84579416/130175760-440b1b02-aae4-4154-9dc5-9dbeb4552b68.png)
--- 
![Figure_2](https://user-images.githubusercontent.com/84579416/130087399-1fe2c277-5d7e-4c86-9227-196983c423a9.png)
---
![Figure_3](https://user-images.githubusercontent.com/84579416/130176365-ce7df126-0614-4377-a981-f06509880aef.png)
---
![Figure_1](https://user-images.githubusercontent.com/84579416/130176345-ec5b7a8f-1fa8-4605-9725-f138e56afa0c.png)
--- 

## Conclusion
Energy consumptsion ranks show completely different depending on the criteria: Country and per Capita in country.\
Iceland has the highest household energy consumption per capita. Norway, Bahrain, Kuwait and Canada are next in line.\
\
Iceland’s high energy consumption is explained by several factors. One is the low cost of electricity production, thanks to an abundance of renewable energy sources (hydropower and geothermal energy). Also, Iceland houses several energy-intensive industries, including aluminium and silicon production, which account for a large proportion of the country’s overall energy consumption. Furthermore, the country’s cold, dark winters contribute to the high demand for electricity.


