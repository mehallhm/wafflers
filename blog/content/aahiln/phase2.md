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

Aside from the project, the speakers and excursions that we had over the past week brought another concept into light: the regulation capabilities of the EU. Unlike the US, which is comparatively lax with its restrictions and gives lobbyists a greater voice in lawmaking, the EU seems to have all of its legislative power held within the Parliament, and there can only be slight modifications in interpretation afterward. In the end, this gives more power to the user, such as with the protections that were provided by the GDPR, but it was also interesting to see how companies such as Microsoft and others (as mentioned in the talk with AmCham) were left scrambling to find a way to satisfy their priorities while complying with the restrictions.

Also, I sincerely believe that I was a baker in another life. Thank you Arno for the experience.
