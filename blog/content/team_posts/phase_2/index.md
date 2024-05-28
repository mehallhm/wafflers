---
title: "Project - Phase II"
date: 2024-05-28
draft: false
description: "Implementation"
tags: ["authors", "config", "docs"]
slug: "phase_two"
authors:
  - "aahil"
  - "anjola"
  - "justin"
  - "michael"
showAuthorsBadges: false
---

## Changes to Phase I

### Updates to Project Description

Enterprises, ranging from local businesses to large corporations are major contributors to global carbon emissions. To provide perspective on the carbon footprints of these entities, this app would provide a feature for corporations to collect information on their own contributions to their country’s footprint. This would allow enterprises to gain insight into their company-wide impact, as well as receive information on the changes needed to be made and the corresponding implementations. To do this, enterprises can additionally gain knowledge from organizations that have dedicated time to researching and combating these issues.

### Updates to User Persona

#### New Persona #3: EcoForward Enterprises

Description: EcoForward Enterprises is an enterprise that sells energy-efficient lighting. Their mission is aligned with trying to become a greener company, but they feel as if there is an improvement that they can invest in to better match that mission. They are interested in trying to reduce their carbon footprint to gain more of their target consumers.

User Story #1: As an enterprise, I want to be able to see the analytics of our carbon emissions so that I can be able to closely estimate our emissions based on transportation, operating emission costs, and more. This would provide an opportunity to reduce costs and invest in more eco-friendly sources within our supply chain.

User Story #2: As an enterprise, I want to be matched with NGOs based on my emission problem areas so that I can gain insight into how to improve. It would be useful to have those problem areas highlighted to me and for the app to generate easy-to-read tags so I know what emission areas I am lacking in.

User Story #3: As an enterprise, I want to understand my contribution to my country’s emissions in comparison to the average company so that I can compete with other companies within the market and obtain an optimal position as a cleaner company to attract more of my target market.

### New Additional Questions:

- What is the contribution of a business to a macro-level impact of CO2 emissions?

  - This question depends on the scale of the involved business—the scope could be on a local or national level and will measure the impact that business practices have on the emissions of a nation and the European Union as a whole. Furthermore, the internal breakdown of emissions will provide a clearer picture of the measures that need to be taken to reduce this impact.

- How can organizations that combat climate change be matched with interested parties?

  - This question combines user/enterprise data with a repository of organizations that combat different sources of climate change, such as an organization combating electric inefficiencies being matched with a person that has a high electricity usage. This question could also encourage partnerships between such organizations and companies currently afflicted with carbon emission-related issues.

### New Data Sources:

-
-

## Database ER Diagrams

|                                                               | Local DDL Diagrams                                        |                                                               |
| ------------------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------- |
| ![Diagram ONE]({{ $image := .Resources.Get "ddl_user.png" }}) | ![Diagram TWO{{ $image := .Resources.Get "sunset.jpg" }}) | ![Diagram THREE]({{ $image := .Resources.Get "sunset.jpg" }}) |

####

{{ $image := .Resources.Get "ddl_global.png" }}

![Global DDL Diagram](../../assets/ddl_global.png)

## [Link to SQL DDL](https://github.com/mehallhm/wafflers)
