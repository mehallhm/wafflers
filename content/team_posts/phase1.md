---
title: "Project - Phase I"
date: 2024-05-21
draft: false
description: "Our Idea"
tags: ["authors", "config", "docs"]
slug: "index"
authors:
  - "aahil"
  - "anjola"
  - "justin"
  - "michael"
showAuthorsBadges: false
---

## Project Description

This app aims to quantify the impact of an individual user on CO2 emissions and climate change as a whole, providing feedback to the user on how they reduce their impact within the European Union.

The carbon personality survey would contain questions similar to "How much do you drive?" and "Do you have a heated house?" which would be used to predict the user's environmental impact. This would be broken down into sectors such as transportation and residential, alongside where that energy most likely came from, such as gas or biofuel. This personalized report would inform the user, based on their existing habits and activity, what impact they are having as well as compare to the stereotypical citizen in their country and across the European Union. In the end, personalized suggestions could be provided to the user in order to improve their carbon footprint.

The app would also feature a macro statistics section, which would allow current trends and future predictions to be displayed. This would allow the user to see the rate at which carbon emissions and climate change are impacting the world and how that might affect their day-to-day lives in the future if no action is taken to slow or stop it. This section can display aggregate trends based on the user's report as well; for example, it could include a graph that demonstrates if everyone in the EU emitted that level of carbon or demonstrate the impact if every citizen lowered their carbon footprint by 5%.

Related to the macro statistics, a policy viewer will be implemented in order to allow the user to see the regulations and laws of particular EU member states (or the EU as a whole) and their impact on climate change initiatives. This would allow the user to not only become more informed and potentially spur political action, but also would allow public workers to judge the efficiency of policy or see if the proposed policy would have an effect. Due to the few, slower, and more static nature of policy, these policy initiatives would most likely be hand-added rather than programmatically collected.

One potential feature would be to have NGOs / nonprofits be able to register with the app (or automatically register based on public records). At the end of the user report, these NGOs could be suggested to the user in order to connect the user with organizations that help mitigate problems the user might have. From an NGO standpoint, they would have a dashboard where they could see how many people they match to as well as anonymous aggregated statistics from the people they match with in order to better understand their target audience.

## User Personas

### Persona #1: EcoUnity Europe

Description: EcoUnity Europe is an NGO that primarily focuses on promoting sustainable development within Europe. Their mission involves trying to gain more active participation from communities in their educational programs, working with businesses to implement sustainable practices, and developing strategies to help communities adapt to the changing climate as well as trying to mitigate any further climate change.

User Story #1: As a non profit organization, it is hard to gain funding in order to have adequate resources to educate the public about potential efforts to mitigate climate change. In order to help EcoUnity Europe’s initiatives, it is essential to try to attract ideal donors who are more willing to support EcoUnity Europe. It would be useful to be able to connect with users based on statistics to gain the interest of people that are already interested in climate change, reducing efforts in gaining more people within the organization.

User Story #2: As an NGO dedicated to helping communities that are the most vulnerable to climate change within the EU, it is essential to make sure that the EcoUnity Europe’s efforts are going to those that need it the most. Having a feature that allows EcoUnity to view community statistics that are vulnerable to climate change NGOs can shift their objectives towards those communities.

User Story #3: As an NGO in order to increase the effectiveness of educational content by potentially personalizing the content towards certain users. In order to produce more heavily personalized educational content EcoUnity Europe would need a feature to view users survey results in order to decide what content would be the most effective in drawing customers to their objectives.

### Persona #2: Natalie Allard

Description: Natalie Allard is a 23-year-old woman living in the city of Paris. She works as a digital nomad for a consulting firm, while her roommate takes college classes as a full-time student. As a result, she is vaguely invested in limiting her carbon footprint, but she enjoys keeping the lights on at home and traveling on weekends that she can spare.

User Story #1: As a member of the general public, I want to find a way to be more conscious of my carbon footprint. With a general sense of my daily consumption, I want to find what habits I currently possess that contribute a disproportionate amount of carbon towards my personal CO2 emissions, such as the fact that I keep my lights on all the time or that I should potentially reduce air travel in favor of train. I can do this by easily filling out a carbon footprint survey that asks me digestible and relevant questions, and provides me a breakdown of my energy consumption by sector, as well as comparisons to other average members of the public.

User Story #2: As a member of the general public, I want to be able to use this information to learn more about my habits and find NGOs and think tanks that have done more research into the impacts of CO2 emission from the sectors to which I currently have a larger contribution. This can be done by selecting the sectors that were highlighted in the survey I completed and matching myself with the NGOs provided in the application.

User Story #3: As a member of the general public, I want to use this information to make an informed decision regarding climate change policy for the upcoming federal and supranational level elections. I want to find more information about the current regulations in place and make decisions on the efficacy of such policies, using the application to give me information specific to me.

### Persona #3: John Davis

Description: John Davis is the secretary of emissions and energy of Belgium. He works closely with fellow members of Belgium’s government as well as EU representatives to optimize energy usage and reduce harmful emissions. He also helps to write policies and regulations based on energy/emissions.

User Story #1: As a governmental emission secretary, I want to be able to select or see all policies related to emissions and analyze their effect on my country and the EU as a whole so that I can see what legislative actions are effective. It would be helpful to see a full breakdown of the types of emissions and quantities or even the types of energy production (wind, solar, coal, etc.).

User Story #2: As a governmental emission secretary, I want to have an intuitive compare tool to see the emissions and energy breakdowns of my country compared to other member states so that I know how well we are doing comparitevly. I would also like to have a predictive model for comparison to see if our emissions are on the right track compared to another country. This would give insight as to whether policy is even necessary or no action is needed.

User Story #3: As a governmental emission secretary, I would like to be able to have a predictive tool in the application so that I can calculate the effect of potential policy. For example, I could input that we need our CO2 emissions to be down 20% and the calculator could output what every citizen of my country would need to decrease their admissions by to achieve this goal. It would be extra helpful if it also outputted ways to reduce emissions by this amount for each user. This would serve to guide future emission and energy regulations.

## Data Sources

- [Eurostat](https://ec.europa.eu/eurostat/web/main/data/database) accessed through [the api](https://wikis.ec.europa.eu/display/EUROSTATHELP/API+-+Getting+started)

  - Would primarily be the energy statistics, along with pieces like population in order to break the energy consumption by sector down into micro statistics

- [NCEI | NOAA](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series)

  - Climate data to make climate based predictions

- [EEA](https://www.eea.europa.eu/data-and-maps/dashboards/emissions-trading-viewer-1)

  - Provides emissions and emission trading data for the EU

- [Worldbank](https://databank.worldbank.org/)

  - Particularly the energy / emissions data. Not the most up to date (most emissions data cuts off at 2014 / 2016) but can provide a larger historical window

- [European Commission](https://commission.europa.eu/energy-climate-change-environment/topics/climate-change_en)
  - Not scrapeable data, but important data to provide the story around legislation and action being taken to combat climate change
  - More background focusses / supplemental information

## Questions:

- Which countries in the EU produce the most harmful emissions or are predicted to in the near future?

  - This question is interesting and can be used by the EU to determine which countries need to reduce their emissions the most. The prediction can indicate whether preventative measures should be taken to ensure emissions don't rise drastically.

- What is the contribution of an individual to a macro-level impact of CO2 emissions?

  - This question combines the user input to the predicted data, as we can measure the given impact of a certain practice and provide a visual on how an individual impacts the EU, and the planet as a whole.

- Is currently implemented policy meant to fight climate change effective?
  - This question will indicate two things: whether policy enacted to fight climate change is having a tangible effect on a country's energy usage, and if not, the sectors that need to be targeted in updated policy to lower carbon footprint.
