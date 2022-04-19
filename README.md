# California-Airbnb-Data-Modeling-Analysis-and-Visualization

In this project we are using Amazon Web Service(AWS) to perform ETL and data visualization.

For all the files we are uploading it to Amazon S3 bucket as s3 is like a data lake.

Using Lambda integration from S3 bucket to Amazon Dynamodb to store geojson file data.

Using AWS Glue we will be doing Extract Transform load (ETL) process on these files to store the clean data into Amazon Redshift data warehouse.

Finally, Using AWS Quicksight tool, will be doing data visualization from amazon redshift by writing sql queries.

![AWSArchitecture](https://user-images.githubusercontent.com/78490598/164093477-16079e3f-af90-459c-af6d-e1b4fc15c82b.png)


**Motivation**

There are over 38300 Airbnb listings in California as of February,2021, which approximates to around 4 houses being rented per square mile. Airbnb has seen an exponential increase in the number of listings in California each year and has gained a lot of popularity. By analysing the number of listings and occupancy rates, we can understand demand rates and also provide metrics for people who would like to make an investment in Airbnb and rent out their properties. Previously collected data and reviews help understand how the occupancy rate can be increased.

**Data Source**

The dataset used for our analysis was taken from the Inside Airbnb website. The dataset consisted of flat files having details regarding the listings, user reviews, and geojson files indicating the location of the listings in each neighborhood within the cities.
We downloaded the datasets for only the chosen counties of California and continued to ingest them into our chosen pro- cessing tools for further steps on the data, involving cleansing, loading into our data warehouse, and analysis.

**Data Modeling**

The following is our data model, and it included the following entities: 

![image](https://user-images.githubusercontent.com/78490598/164098283-7d86ffa9-f957-4055-b6c6-8ad79752d77d.png)

**SQL Queries**

The data was analyzed using SQL queries. A sample of our data analysis using SQL queries in Redshift is given below. 
 
Figure 3: SQL Query in AWS Redshift - Neighborhood, price, reviews correlation 
 
Figure 4: Query result table - Neighborhood, price, reviews the correlation  
![image](https://user-images.githubusercontent.com/78490598/164100162-3ed512ab-4054-4aab-b6fc-2dfb004fb1f5.png)

**Visualization**

We used AWS QuickSight to visualiza the results of the SQL Queries and Analyze the trends of the Airbnb dataset.

<img width="1056" alt="Screen Shot 2022-04-19 at 2 08 57 PM" src="https://user-images.githubusercontent.com/78490598/164102325-fb100c64-338f-4029-8441-ec7132d564d8.png">

