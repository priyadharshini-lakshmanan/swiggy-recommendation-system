Swiggy Restaurant recommendation system
---------------------------------------
A data analysis project exploring 148,541 Swiggy restaurant records across India using K-Means clustering to segment restaurants based on ratings, cost, cuisine, and location.

Overview
--------
Dataset: 

148,541 restaurants → Cleaned to 74,460 from top 10 Indian cities

Analysis: 

Data cleaning, feature engineering, and unsupervised learning

ML Model:

K-Means clustering (5 clusters) on 1,739 encoded features

Top Cities: 

Bangalore (14,402), Delhi (14,048), Pune (12,412), Chennai (9,940)

Features: 

Restaurant ratings, cost analysis, cuisine patterns, geographic distribution

Tech Stack: 

Python, Pandas, Scikit-learn, Jupyter Notebook

Output: 

final_data.csv with cluster assignments, encoder.pkl for deployment

Use Case: 

Restaurant segmentation, market analysis, recommendation systems


-----------------------------------------------------------------

Installation:

bashpip install pandas numpy scikit-learn jupyter

jupyter notebook swiggy.ipynb
