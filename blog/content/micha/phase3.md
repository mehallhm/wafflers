---
title: "Phase III Reflection"
date: 2024-06-06
draft: false
slug: "3"
tags: ["reflection"]
authors:
    - "michael"
---

### Project Reflection

This project phase was dominated by implimentation of the machine learning model that was partially discovered in Phase II. However, as I was building it, nearly every part had to go back to the drawing board. Starting off, the scraper / parser combination I was using to get the data from Eurostat was made for a three dimentional table, not some of the more complex five or six dimentions that some of the new data I found was structured as. As a result, I could either roll my own implementation again or use a library; I choose the later and used fthe SDMX standard after our visit to Eurostat. After discovering some of its odities, such as what needed to be capitalized and what did not, it turned out to be much easier to pull data them my hand rolled solution. After that was switched out, other pieces such as merging the data and standardizing could be pulled from the previous codebase with light moditifcations.

After getting a new data pipeline constructed, I also went back to the beginning for what data to use in order to draw the conclusion of carbon emissions. First, choosing which interpretation of "Carbon Emissions" had to be made, and, after a little general topic research, I dived into specifics for areas that make up the global carbon emission footprint. These primarily include Energy, Transportation, Agriculture, and Industry. Since we wanted to focus on residential people for this first model, I found great datasets for household energy and transportation, after bouncing ideas off of some of the professors. After finding the data and cleaning it using linear regression within each block of observations, I constructed the model to find that the original set of features insufficiant. To risk repeat myself from the team post, we settled on total household energy rather than by household sector, and used fuel as a proxy for transportation. However, even when using this smaller dataset, we ran into issues of overfitting, caused by the one-hot encoded country data. After dicussion with one of the professors, it was determined that the country was not strictly necessary for the model as the data was linear enough without it. After that, the model was good enough for now, and was tested using LOO-CV to find a final R2.

### Belgium Reflection

While not in regards to Belgium, the lecture on the GDPR was one of my favorite guest speakers. Not only was the speaker incredibly knoledgeable, he also operated on a shared basis of understanding, allowing him to skip some of the technical aspects that we already knew. The law and legislation that the EU has been pushing and the reasoning _why_ is super interesting and could potentially give Europe that leg up which the legislators belive it will. I have always admired the digital restraits that the EU puts on companies in favor of people and hearing an expert talk about one specifc one was very interesting. He also aroused something in me that enjoys that type of work where it operates in both a technical aspect as well as, in this case, a legal one.
