---
title: "Phase III Reflection"
date: 2024-06-06
draft: false
slug: "3"
tags: ["reflection"]
authors:
  - "aahiln"
---

Phase III was, definitely, even more work.
Due to the nature of our project, a lot of the database work we had already done and routing for our API calls were dependent on the results of the linear regression that Michael had been doing on the DS end of things. As a result, the majority of the week was spent doing minor housekeeping tasks such as creating the landing page, which Justin did. (I set the theme though!)

Once Michael had completed some regression, I took lead on the implementation of the user survey in Streamlit and all of those related calls. Since we were assuming that the user was simply retaking the survey, most of the API calls were thus PUTs and GETs. These took a minute to debug, but the next step was to finally integrate the ML model...to which I found out that the model was currently being overfitted. This meant that the data collected for Country, Water Heating, Electricity Usage, and Cooking was unnecessary, so I left the survey questions and routes intact, but they aren't getting called in the final predictive step.

Implementing the predictive step took a long time due to a few issues that came up, namely with the Docker image not installing the packages from requirements.txt properly, and then with a few model bugs that had to be ironed out. Upon figuring out the type (float, not a tuple!) of the outputs and implementing the code based on that, we were able to get a final predictive carbon footprint. The next step would be to add a train button into the UI, because our betavals are currently hard-coded into the SQL, and to use the Country data to provide a comparison of your carbon footprint. Good progress regardless!
