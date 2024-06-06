---
title: "Project - Phase II"
date: 2024-05-28
draft: false
description: "Implementation"
tags: ["authors", "config", "docs"]
slug: "phase_three"
authors:
  - "aahil"
  - "anjola"
  - "justin"
  - "michael"
showAuthorsBadges: false
---

# API routes and purposes 

### User Routes 
u/UserCars (GET)
Gets all car survey data history for the user 
u/UserAddCar (PUT) 
Allows the user to add additional car survey data 

u/UserResidential (GET)
Gets all residential survey data history for the user

u/UserFlights (GET)
Gets all flight survey data history for the user

u/UserTransport (GET)
Gets all transport survey data history for the user

u/UserAddRes (PUT)
Updates this user's residential data based on survey


### NGO Routes

n/NGOupdate (PUT)
Updates the NGO given filled out data in NGO table

n/tags (GET)
Gets the tag description for all tags for the NGO user

n/EnterpriseMatch (GET)
Gets the all matching enterprise names and descriptions based on tags

n/ngomine (GET)
Gets all my NGO data from the NGO table

n/UserMatch (GET)
Gets all of the matching users based on tags

n/TagDelete
Allows NGOs to delete tags that they were associated with 
n/NGOadd
Allows NGOs to add tags that they want to be associated with 


### Enterprise Routes

e/tags (GET)
Gets all of the enterprise’s tags from database

e/NGOMatch (GET)
Gets all of the matching NGO's based on tags

e/EntCompare (GET)
Gets my emissions, my country's, and the average of other companies in same country 

e/EntSupplyChain (GET)
Gets all the supply chain history for this enterprise

e/EntCosts (GET)
Gets all the operating cost history for this enterprise

e/EntFlights (GET)
Gets all the flights history for this enterprise

# Application Protype 
## Database ER Diagrams


| User Homescreen                   | Enterprise Homescreen                        | NGO homescreen  Diagram                   |
| ----------------------------------- | --------------------------------------------- | --------------------------------- |
| ![User Homescreen](./userhomepage.jpg) | ![Enterprise Homescreen](./enterprisehomescreen.jpg) | ![NGO Homescreen](./ngohomepage.jpg) |
These are images of each of the user personas. The homescreen for each user persona allows them to implement the features mentioned in their respective user persona stories. The main features for users and enterprises include taking surveys to gather further information, while the NGO persona does not take a survey. Instead, NGOs select the tags they want to be associated with and are matched with users based on these tags.

| User Homescreen                   | Enterprise Homescreen   
![NGO Survey](./ngosurvey.jpg) | [NGO Match](./ngomatch.jpg)
In the NGO user persona, NGOs decide which tags they want to be associated with. Based on these tags, they receive a list, similar to the example above, allowing them to see which users and enterprises they have been matched with.

User Survey 
![User Survey](./usersurvey.jpg) 
In the general user persona, users take a survey, and based on this survey data, the app interacts with a machine learning model to estimate future carbon emissions and provide data on their current carbon emissions.

Enterprise Survey 
![Enterprise Survey](./enterprisehome.jpg) 
Enterprises, similar to general users, also take a survey. This survey allows them to match with general users and NGOs. 






