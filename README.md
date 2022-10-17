# Reddit-NLP-Project
Northwestern Data Science Class w/ Andrew Goodwin, Joe Mazanec, Sodiq Algabada

## Data 

3GB dataset from Hugging Face of Reddit posts with the author of the post, body of the post and a generic subreddit ID.

https://huggingface.co/datasets/reddit/tree/main

## Backend ETL

Load into Databricks via Hugging Face endpoint for tokenization with PySpark. PySpark and Pandas for data preprocessing and data manipulation. Create a subset of data that holds the top 10 subreddits for classifier model. Load both the full dataset and the subset dataset into Amazon Web Services postgreSQL database. Access database via pgAdmin on local machine and connect to Tableau for visualizations.

## Visualizations

Visualize full dataset trends with Tableau - what words are most popular per subreddit, sentiment analysis. 

## Machine Learning Model

Use Naive Bayes and Multiclass Classification Evaluator to determine top performing classifier model on subset of reddit data containing the top 10 subreddits by post volume. Based on the top performing Multiclass Classification Evaluator model, manually train a classifier model to predict, given a new post, what subreddit to which it most likely belongs. 

## Division of Responsibilities (Flexible)

- Tokenize and Hashing with PySpark (Everyone)
- Preprocess with Pandas and PySpark (Andy)
- Load data from AWS to Databricks (Everyone)
- Visualize with Tableau (Sodiq)
- Use Multiclass Classification Evaluator to sift through classifier models (Tim & Joe)
- Manually train and tune hyperparameters of classifier model (Tim & Joe)

## Tableau Dashboard
link : https://public.tableau.com/app/profile/sodiq.alagbada/viz/reddit_16659191519010/Dashboard1?publish=yes

![Tableau SC](https://user-images.githubusercontent.com/104107204/196059576-ff0485ed-948b-4d5a-a0ee-598bf4d91fa4.jpeg)


