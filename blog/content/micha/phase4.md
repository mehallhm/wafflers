---
title: "Phase IV Reflection"
date: 2024-06-10
draft: false
tags: ["reflection"]
authors:
    - "michael"
---

## Final Project Contributions

My contributions to the final project include both machine learning models as well as some various data plumbing pieces around them. Since Phase III, I have created the TF-IDF and Cosine Similarity model which recommends NGOs by matching user and organizations bios. In order to create this model data had to be collected, since performing machine learning on generated data would not yield useful results; Wikipedia pages on environmental organizations were scraped, cleaned, and then used to train the TF-IDF. However, in order to ensure that the database started with these faked organizations (that contain real bios), I wrote a script that would generate the SQL bootstrap file with all the data in it. I wanted to store a vectorized version of each bio in the db as well, in order to reduce computation when predicting and to do this I had to write a little custom encoder and decoder to store the sparse matrices that the verctors were stored in.

In addition, I wrote the streamlit frontend and api endpoint to communicate with the NGO recomendations algorithm. This was just a little different than the machine learning code, since I had to learn a little bit about Flask and Streamlit in order to correctly get everything wired up. This also included a little refactoring to both the api server and streamlit frontend to ensure PEP compliance as well as readable code.

## Challenges and Joys

The most challenging part of the project was finding data and features for the linear regression model. I think this was due to a couple of things at the same time - first, I was still learning the concepts so while I knew them, I had not yet fully internalized them and thus I was a little slower and clunkier in my application of the tools. I felt like things that should be easy were unecessarily difficult and visa versa, compounding to a little bit of frustration at not being able to go in the direction I thought I could. Additonally, my method at getting data from Eurostat was... bad since it was a parser I made rather than using a standard and library for it. This gave me difficulties since sometimes the data was actually not correlated and sometimes my parser was just acting up. Using standards from the beginning and not solving already solved problems would have helped a lot. Finally, I also was trying to put together a puzzle and never stepping back - I did not research what actually affected emissions until after I had seriously invested time into doing data collection. Once I realized where to go, getting there was much easier. Overall, these little troubles compounded to make the task of finding what data to work with more difficult than I think it should have been.

On the other hand, the part I found most enjyable was writing the TF-IDF and Cosine Similarity model. The idea of matching based on text rather than numerical features seemed super interesting, and I started doing research into what exactly that entailed. In contrast to above, making this model felt much more defined since I did the work beforehand to understand what I needed and how to manipulate it into the form that would be useful. In addition, at this point I felt much more confortable in Python and so could quickly execute my ideas. It was just really fun to make the model and it spitting recommendations out at the end was incredibly rewarding; even though I knew what it was doing it still felt a little magical.

## Resume Blob

Below is a little project section on what it might look like (I have never written one of these before 🥶):

**Carbon Connect**

-   Developed real-time carbon footprint calculator with a linear regression model
-   Paired users to real environmental organizations based on a user biography
-   Created with a team of four while studying abroad in Belgium
