---
title: "Phase II Reflection"
date: 2024-05-28
draft: false
slug: "2"
tags: ["reflection"]
authors:
  - "aahiln"
---

Phase II was pretty long. The vast majority of the week was spent ideating and deciding in group-wide discussions about what attributes would be represented in the data, both for the regression model and the stored data. Michael and I spoke a bit about the regression that would be done, and I lent an ear to the eureka moments when a working dataset was found. On the database side of things, I created the ER Diagram for the general public user, which turned out to be the basis of the newly created enterprise entity, and was a bulk of the initial ER diagram. However, we ended up having to remove the Government entity from our user personas because of the potential complications, which set us back to updating a few of the decisions made during Phase I, which I updated while Justin and Anjola contributed to the initial wireframing. After that, we meshed together our local ER diagrams to create the global diagram, and began work on the DDL for the tables. There was a bit of confusion on whether some of the tables could have been introduced as attributes instead, but the interplay that we decided on later and the potential option to store the data provided enough reason to keep it separate. The DDL was a quite a bit of work, but we split up the tables (thanks to Justin's conversion of the line diagram to a table version) and got it done.

Looking forward, we need to make a decision on two things: a name for the project, and the type of data that is being stored as "emissions data". For now, the intention is to hold that data as an int representing the number of tons of carbon emissions, but as the data was cleaned and new data sets are pulled in, we could further expand this attribute to include a specific amount of money lost, or a proportion compared to an average.
