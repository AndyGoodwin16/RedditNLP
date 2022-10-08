# Reddit-NLP-Project
Northwestern Data Science Class w/ Andrew Goodwin, Joe Mazanec, Sodiq Algabada

## Data 

3GB dataset from Hugging Face of Reddit posts with the author of the post, body of the post and a generic subreddit ID.

https://huggingface.co/datasets/reddit/tree/main

## Backend ETL

Load into Databricks via Hugging Face endpoint for tokenization with PySpark. Pandas for data preprocessing and data manipulation. Create a subset of data that holds the top 10 subreddits for classifier model. Load both the full dataset and the subset dataset into Amazon Web Services postgreSQL database. Access database via pgAdmin on local machine and connect to Tableau for visualizations.

## Visualizations

Visualize full dataset trends with Tableau - what words are most popular per subreddit, sentiment analysis. 

## Machine Learning Model

Use PyCaret to determine top performing classifier model on subset of reddit data containing the top 10 subreddits by post volume. Based on the top performing PyCaret model, manually train a classifier model to predict, given a new post, what subreddit to which it most likely belongs. Host application on Heroku.

## Division of Responsibilities (Flexible)

- Load dataset into Databricks (Everyone)
- Tokenize with PySpark (Everyone)
- Preprocess with Pandas (Andy)
- Load into AWS postgreSQL database (Everyone)
- Connect database to Tableau (Sodiq)
- Visualize with Tableau (Sodiq)
- Use PyCaret to sift through classifier models (Tim & Joe)
- Manually train and tune hyperparameters of classifier model (Tim & Joe)
- Host on Heroku (Everyone)




